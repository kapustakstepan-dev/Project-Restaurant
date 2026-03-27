import os
import secrets
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError
from flask_mail import Mail, Message

from back.BD.online_restaurant_db import Session, Users, Menu, Reservation, Orders, init_db

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret-key')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER', 'RetroBite <noreply@retrobite.com>')

mail = Mail(app)


@login_manager.user_loader
def load_user(user_id):
    with Session() as db_session:
        return db_session.get(Users, int(user_id))


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/menu')
def menu():
    with Session() as db_session:
        all_positions = db_session.query(Menu).filter_by(active=True).all()
    return render_template('menu.html', all_positions=all_positions)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nickname = request.form['username']
        email = request.form['email']
        password = request.form['password']

        with Session() as db_session:
            if db_session.query(Users).filter_by(nickname=nickname).first():
                flash("Username already exists!")
                return redirect(url_for('register'))

            if db_session.query(Users).filter_by(email=email).first():
                flash("Email already registered!")
                return redirect(url_for('register'))

            user = Users(nickname=nickname, email=email, role='user')
            user.set_password(password)

            try:
                db_session.add(user)
                db_session.commit()
            except IntegrityError:
                db_session.rollback()
                flash("Email already exists!")
                return redirect(url_for('register'))

        flash("User registered successfully!")
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nickname = request.form['username']
        password = request.form['password']

        with Session() as db_session:
            user = db_session.query(Users).filter_by(nickname=nickname).first()
            if user and user.check_password(password):
                login_user(user)
                flash(f"Welcome, {user.nickname}!")
                return redirect(url_for('menu'))
            else:
                flash("Invalid username or password")

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for('login'))


@app.route('/position/<int:position_id>', methods=['GET', 'POST'])
def position(position_id):
    with Session() as db_session:
        pos = db_session.query(Menu).filter_by(id=position_id).first()

    if not pos:
        return "Position not found", 404

    if 'basket' not in session:
        session['basket'] = {}

    basket = session['basket']

    if request.method == 'POST':
        num = int(request.form.get('quantity', 1))
        basket[str(pos.id)] = basket.get(str(pos.id), 0) + num
        session['basket'] = basket
        return redirect(url_for('position', position_id=position_id))

    return render_template("position.html", position=pos)


@app.route('/create_order', methods=['GET', 'POST'])
@login_required
def create_order():
    basket = session.get('basket', {})
    if not basket:
        return redirect(url_for('menu'))

    with Session() as db_session:
        basket_items = []
        total_price = 0
        for item_id, quantity in basket.items():
            try:
                item = db_session.query(Menu).get(int(item_id))
                if item:
                    basket_items.append({'item': item, 'quantity': quantity})
                    total_price += item.price * quantity
            except Exception as e:
                print(f"Error fetching menu item {item_id}: {e}")

        if request.method == 'POST':
            # Create Order
            try:
                order = Orders(
                    order_list=basket,
                    total_price=total_price,
                    user_id=current_user.id,
                    state='confirmed',
                    order_time=datetime.now()
                )
                db_session.add(order)
                db_session.commit()
                order_id = order.id
            except Exception as e:
                db_session.rollback()
                print(f"Database error creating order: {e}")
                # Fallback: create order without total_price if column missing
                try:
                    order = Orders(
                        order_list=basket,
                        user_id=current_user.id,
                        state='confirmed',
                        order_time=datetime.now()
                    )
                    db_session.add(order)
                    db_session.commit()
                    order_id = order.id
                except Exception as e2:
                    db_session.rollback()
                    return {"success": False, "error": str(e2)}

            action = request.form.get('action')
            if action == 'send_email':
                try:
                    msg = Message(f"Your RetroBite Receipt #{order_id}",
                                recipients=[current_user.email])
                    msg.body = f"Order ID: #{order_id}\nTotal: ${total_price:.2f}\nItems: {basket}\nThank you for choosing RetroBite!"
                    mail.send(msg)
                    flash("Receipt sent to your email!")
                except Exception as e:
                    # Log but carry on - order is already saved
                    print(f"Flask-Mail error (Order #{order_id} safe): {e}")

            session.pop('basket', None)
            
            # Return JSON for AJAX modal
            return {
                "success": True,
                "order_id": order_id,
                "total": total_price,
                "items": [{ "name": bi['item'].name, "qty": bi['quantity'], "price": bi['item'].price } for bi in basket_items],
                "date": datetime.now().strftime("%Y-%m-%d %H:%M")
            }

    return render_template('create_order.html', basket=basket, total_price=total_price)


@app.route('/add_to_basket/<int:id>', methods=['POST'])
def add_to_basket(id):
    num = int(request.form.get('quantity', 1))

    if 'basket' not in session:
        session['basket'] = {}

    basket = session['basket']
    basket[str(id)] = basket.get(str(id), 0) + num
    session['basket'] = basket

    return redirect(url_for('my_orders'))


@app.route('/my_orders')
def my_orders():
    basket = session.get('basket', {})
    items = []

    with Session() as db_session:
        for id_str, quantity in basket.items():
            try:
                item_id = int(id_str)
            except ValueError:
                continue
            item = db_session.query(Menu).filter_by(id=item_id).first()
            if item:
                items.append({
                    "item": item,
                    "quantity": quantity
                })

    return render_template("my_orders.html", items=items)


@app.route('/reservation', methods=['GET', 'POST'])
@login_required
def reservation():
    if request.method == 'POST':
        time_start_str = request.form['datetime']
        time_start = datetime.strptime(time_start_str, "%Y-%m-%dT%H:%M")
        table_type = request.form['table_type']

        if time_start < datetime.now():
            flash("No se pueden realizar reservas en el pasado")
            return redirect(url_for('reservation'))

        with Session() as db_session:
            res = Reservation(
                time_start=time_start,
                type_table=table_type,
                user_id=current_user.id
            )
            db_session.add(res)
            db_session.commit()

        flash("Reservation created successfully!")
        return redirect(url_for('my_reservations'))

    return render_template('reservation.html')


@app.route('/my_reservations')
@login_required
def my_reservations():
    with Session() as db_session:
        res_list = db_session.query(Reservation).filter_by(user_id=current_user.id).all()
        order_list = db_session.query(Orders).filter_by(user_id=current_user.id).all()
    return render_template('my_reservations.html', reservations=res_list, orders=order_list)


@app.route('/delete_reservation/<int:id>', methods=['POST'])
@login_required
def delete_reservation(id):
    with Session() as db_session:
        res = db_session.query(Reservation).filter_by(id=id, user_id=current_user.id).first()
        if res:
            db_session.delete(res)
            db_session.commit()
            flash("Reservation deleted successfully!")
    return redirect(url_for('my_reservations'))



@app.route('/admin')
@login_required
def admin():
    if current_user.role != 'admin':
        return redirect(url_for('home'))

    with Session() as db_session:
        items = db_session.query(Menu).all()
        try:
            orders = db_session.query(Orders).all()
        except Exception as e:
            print(f"Orders query failed (likely missing total_price): {e}")
            db_session.rollback()
            # If query fails, we might be hitting the missing column. 
            # In a real app we'd fetch specific columns, but here we just try to recover.
            orders = [] 
        
        reservations = db_session.query(Reservation).all()
        users_list = db_session.query(Users).all()

    return render_template('admin.html', items=items, orders=orders, reservations=reservations, users=users_list)


@app.route('/admin/users')
@login_required
def all_users():
    if current_user.role != 'admin':
        return redirect(url_for('home'))

    with Session() as db_session:
        users_list = db_session.query(Users).all()

    return render_template('admin.html', active_tab='users', users=users_list)


@app.route('/admin/add', methods=['POST'])
@login_required
def admin_add_item():
    if current_user.role != 'admin':
        return redirect(url_for('home'))

    name = request.form['name']
    price = float(request.form['price'])
    description = request.form['description']
    image_url = request.form.get('image_url', 'burger.jpg')

    with Session() as db_session:
        new_item = Menu(name=name, price=price, description=description, image_url=image_url, active=True)
        db_session.add(new_item)
        db_session.commit()
        flash("Item added successfully!")

    return redirect(url_for('admin'))


@app.route('/admin/edit/<int:id>', methods=['POST'])
@login_required
def admin_edit_item(id):
    if current_user.role != 'admin':
        return redirect(url_for('home'))

    with Session() as db_session:
        item = db_session.query(Menu).get(id)
        if item:
            item.name = request.form['name']
            item.price = float(request.form['price'])
            item.description = request.form['description']
            item.active = 'active' in request.form
            db_session.commit()
            flash("Item updated successfully!")

    return redirect(url_for('admin'))


@app.route('/admin/delete/<int:id>', methods=['POST'])
@login_required
def admin_delete_item(id):
    if current_user.role != 'admin':
        return redirect(url_for('home'))

    with Session() as db_session:
        item = db_session.query(Menu).get(id)
        if item:
            db_session.delete(item)
            db_session.commit()
            flash("Item deleted successfully!")

    return redirect(url_for('admin'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/<path:filename>.html')
def remove_html(filename):
    return redirect(f'/{filename}')


if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5001)

import os
import secrets
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError

from back.BD.online_restaurant_db import Session, Users, Menu, Reservation, Orders, init_db

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret-key')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


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
    if request.method == 'POST' and basket:
        with Session() as db_session:
            order = Orders(
                order_list=basket,
                order_time=datetime.now(),
                state='preparing',
                user_id=current_user.id
            )
            db_session.add(order)
            db_session.commit()
        session.pop('basket', None)
        flash("Order created successfully!")
        return redirect(url_for('my_orders'))
    return render_template('create_order.html', basket=basket)


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


@app.route('/menu_check', methods=['GET', 'POST'])
@login_required
def menu_check():
    if current_user.role != 'admin':
        return redirect(url_for('home'))

    if 'csrf_token' not in session:
        session['csrf_token'] = secrets.token_hex(16)

    if request.method == 'POST':
        if request.form.get("csrf_token") != session['csrf_token']:
            return "Blocked", 403

        position_id = request.form.get('pos_id')
        if not position_id:
            return "Bad request", 400

        position_id = int(position_id)

        with Session() as db_session:
            pos = db_session.query(Menu).filter_by(id=position_id).first()
            if pos:
                if 'change_status' in request.form:
                    pos.active = not pos.active
                elif 'delete_position' in request.form:
                    db_session.delete(pos)

                db_session.commit()

    with Session() as db_session:
        all_positions = db_session.query(Menu).all()

    return render_template('check_menu.html',
                           all_positions=all_positions,
                           csrf_token=session["csrf_token"])


@app.route('/all_users')
@login_required
def all_users():
    if current_user.role != 'admin':
        return redirect(url_for('home'))

    with Session() as db_session:
        all_users_list = db_session.query(Users).all()

    return render_template('all_users.html', all_users=all_users_list)


@app.route('/admin')
@login_required
def admin():
    if current_user.role != 'admin':
        return redirect(url_for('home'))

    return render_template('admin.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/<path:filename>.html')
def remove_html(filename):
    return redirect(f'/{filename}')


if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5001)

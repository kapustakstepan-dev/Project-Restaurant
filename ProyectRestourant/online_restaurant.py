import os
import sys
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from datetime import datetime
from sqlalchemy.exc import IntegrityError

from back.BD.online_restaurant_db import Session, Users, Menu, Reservation, Orders, init_db

app =Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret-key')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    with Session() as db_session:
        return db_session.query(Users).get(int(user_id))


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

            user = Users(nickname=nickname, email=email, role='client')
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


@app.route('/position/<name>', methods=['GET', 'POST'])
def position(name):
    with Session() as db_session:
        position = db_session.query(Menu).filter_by(name=name).first()

    if request.method == 'POST':
        num = int(request.form.get('num', 1))
        num = min(num, 10) # Max 10 per product
        if 'basket' not in session:
            session['basket'] = {}
        basket = session['basket']
        basket[name] = basket.get(name, 0) + num
        session['basket'] = basket
        flash(f"Added {num} x {name} to basket!")
        return redirect(url_for('position', name=name))

    return render_template('position.html', position=position)


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


@app.route('/my_orders')
@login_required
def my_orders():
    print("My Orders accessed", file=sys.stderr)
    with Session() as db_session:
        orders = db_session.query(Orders).filter_by(user_id=current_user.id).all()
    return render_template('my_orders.html', orders=orders)


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
    if current_user.nickname != 'Admin':
        return redirect(url_for('home'))

    # Initialize CSRF token if not present
    if 'csrf_token' not in session:
        import secrets
        session['csrf_token'] = secrets.token_hex(16)

    if request.method == 'POST':
        if request.form.get("csrf_token") != session['csrf_token']:
            return "Blocked", 403

        position_id = request.form['pos_id']
        with Session() as cursor:
            position = cursor.query(Menu).filter_by(id=position_id).first()

            if position:
                if 'change_status' in request.form:
                    position.active = not position.active
                elif 'delete_position' in request.form:
                    cursor.delete(position)
                cursor.commit()

    with Session() as cursor:
        all_positions = cursor.query(Menu).all()

    return render_template('check_menu.html', all_positions=all_positions, csrf_token=session["csrf_token"])


@app.route('/all_users')
@login_required
def all_users():
    if current_user.nickname != 'Admin':
        return redirect(url_for('home'))

    with Session() as cursor:
        all_users_list = cursor.query(Users).all()

    return render_template('all_users.html', all_users=all_users_list)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/<path:filename>.html')
def remove_html(filename):
    return redirect(f'/{filename}')



if __name__ == '__main__':
    init_db()
    app.run(debug=True)

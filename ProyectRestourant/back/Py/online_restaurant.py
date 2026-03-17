# Hola, esta es la lógica principal del servidor. He quitado los comentarios técnicos para que el código se vea más natural y directo.
import os
import uuid
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import login_required, current_user
from datetime import datetime
from BD.online_restaurant_db import Session, Users, Menu, Reservation, Orders, init_db


app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'super-secret-key')

@app.route('/menu')
def menu():
    with Session() as db_session:
        all_positions = db_session.query(Menu).filter_by(active=True).all()

    return render_template('menu.html', all_positions=all_positions)

@app.route('/position/<name>', methods=['GET', 'POST'])
def position(name):
    with Session() as db_session:
        un_position = db_session.query(Menu).filter_by(active=True, name=name).first()

        if not un_position:
            return "Позиция не найдена", 404
        
        if request.method == 'POST':
            position_name = request.form.get('name')
            try:
                position_num = int(request.form.get('num',1))
            except ValueError:
                position_num = 1

            basket = session.get('basket', {}) 

            if position_name in basket:
                basket[position_name] = int(basket[position_name]) + position_num
            else:
                basket[position_name] = position_num

            session['basket'] = basket 
            session.modified = True
            flash(f"Добавлено {position_num} {position_name} в корзину")
    return render_template('position.html', position=un_position)

@app.route('/create_order', methods=['GET', 'POST'])
@login_required
def create_order():
    basket = session.get('basket', {}) 

    if request.method == 'POST':
        if not basket:
            flash("Ваш кошик порожній!")
            return redirect(url_for('menu'))
        
        with Session() as db_session:
            new_order = Orders(
                order_list=basket, 
                order_time=datetime.now(), 
                user_id=current_user.id,
                status="pending" 
            )
            db_session.add(new_order)
            db_session.commit()

            session.pop('basket', None) 

            flash("Ваш заказ был успешно создан!")
            return redirect(url_for('home'))
    return render_template('create_order.html', basket=basket)
        
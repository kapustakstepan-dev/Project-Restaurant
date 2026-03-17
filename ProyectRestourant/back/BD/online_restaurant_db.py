# ¡Listo! Aquí tenemos toda la estructura de la base de datos limpia y organizada para que todo funcione de maravilla.
import os
import bcrypt
from datetime import datetime
from typing import List, Dict
from sqlalchemy import create_engine, String, ForeignKey, Boolean, DateTime, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship, sessionmaker, DeclarativeBase
from sqlalchemy.dialects.postgresql import JSONB
from flask_login import UserMixin
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine) 

class Base(DeclarativeBase):
    pass

class Users(Base, UserMixin):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password = Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    role: Mapped[str] = mapped_column(String(20), default='client')

    reservation: Mapped[List['Reservation']] = relationship(back_populates='user')
    orders: Mapped[List['Orders']] = relationship(back_populates='user')

    def set_password(self, password: str):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

class Menu(Base):
    __tablename__ = 'menu'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    weight: Mapped[str] = mapped_column(String(100))
    ingredients: Mapped[str] = mapped_column(Text)
    description: Mapped[str] = mapped_column(Text)
    price:Mapped[int] = mapped_column(Integer)
    active: Mapped[bool] = mapped_column(Boolean, default=True)
    file_name: Mapped[str] = mapped_column(String(200))

class Reservation(Base):
    __tablename__ = 'reservations'
    id:Mapped[int] = mapped_column(primary_key=True)
    time_start: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    type_table: Mapped[str] = mapped_column(String(20))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped['Users'] = relationship(back_populates='reservation')

class Orders(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    order_list: Mapped[Dict] = mapped_column(JSONB)  
    order_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    state: Mapped[str] = mapped_column(String(50), default='pending')
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped['Users'] = relationship(back_populates='orders')


def init_db(): 
    print("Створення таблиць у базі даних")
    Base.metadata.create_all(engine)
    print("Таблиці успішно створені")

if __name__ == "__main__":
    init_db()
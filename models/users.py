import requests

import connect_db
from models import Base
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
import models.products
import models.tickets
import models.orders
login = None
pasword = None
user_id =None


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    points = Column(Integer)
    ticket = relationship('Ticket', back_populates='user_id')
    order = relationship('Orders', back_populates='user')



    @staticmethod
    def is_exist(username: str) -> bool:
        with connect_db.Session(autoflush=False, bind=connect_db.engine) as db:
            res = db.query(User)
            if res.count():
                for element in res:
                    if element.username == username:
                        print('Пользователь есть в системе')
                        return False
                    else:
                        return True
            else:
                return True
    @staticmethod
    def create_user(username:str, password:str, points:int=0):
        with connect_db.Session(autoflush=False, bind=connect_db.engine) as db:
            tmp = User(username=username, password=password, points=points)
            db.add(tmp)
            db.commit()
            print('Пользователь создан')


    # Увеличение баланса
    @staticmethod
    def update_points(id):
        with connect_db.Session(autoflush=False, bind=connect_db.engine) as db:
            point = db.query(User).filter(models.users.User.id == id)
            for element in point:
                element.points += 20
            db.commit()

    # Уменьшение баланса
    @staticmethod
    def decrease_pointss(id: int, cost: int ):
        with connect_db.Session(autoflush=False, bind=connect_db.engine) as db:
            point = db.query(User).filter(User.id == models.users.user_id)
            print(models.users.user_id)
            for element in point:
                element.points -= cost
                db.commit()

    #Просмотр баланса
    @staticmethod
    def balanse_user():
        with connect_db.Session(autoflush=False, bind=connect_db.engine) as db:
            res = db.query(User).filter(User.id==models.users.user_id)
            for element in res:
                return element.points

# отображение пользователя
    @staticmethod
    def show_profile(user_id: int):
        print(f'==={login}===')
        print(f'Поинтов: {User.balanse_user()}')
        print(f'\nЗаказы:\n\n')
        print()
        date_order = 'Дата заказа'
        count_order = 'Кол-во'
        sum_order = 'Сумма'
        name = 'Название товара'
        print(f'{date_order:48}{count_order:25}{sum_order:18}{name:41}\n{"-" * 150}')

        with connect_db.Session(autoflush=False, bind=connect_db.engine) as db:
            res = db.query(models.orders.Orders.order_datetime,
                           models.orders.Orders.count,
                           models.products.Product.cost * models.orders.Orders.count,
                           models.products.Product.name

                           ).join(models.products.Product).filter(models.orders.Orders.user_id == models.users.user_id)
            for element in res:
                print(f'{element[0]}{element[1]:25}{element[2]:25}{element[3]:>30}')










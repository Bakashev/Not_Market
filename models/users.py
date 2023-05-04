import requests

import connect_db
from models import Base
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
import models.products
login = None
pasword = None


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
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

def create_user(username:str, password:str, points:int=0):
    with connect_db.Session(autoflush=False, bind=connect_db.engine) as db:
        tmp = User(username=username, password=password, points=points)
        db.add(tmp)
        db.commit()
        print('Пользователь создан')


def user_entry():
    login_reg = input('Введите свой логин >')
    password_reg = input('Введите свой пароль >')
    with connect_db.Session(autoflush=False, bind=connect_db.engine) as db:
        res = db.query(User)
        for element in res:
            if element.username == login_reg and element.password == password_reg:
                while True:
                    first_user_comand = '>\tТовары'
                    second_user_comand = '>\tКупить'
                    third_user_comand = '>\tПрофиль'
                    four_user_comand = '>\tТикет'
                    print(f'{first_user_comand}\n{second_user_comand}\n{third_user_comand}\n{four_user_comand}\n')
                    global login
                    global pasword
                    login = login_reg
                    pasword = password_reg
                    user_comand = input('Выберите команду:')
                    if user_comand == 'Товары':
                         models.products.get_product()








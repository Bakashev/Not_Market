import sqlalchemy.exc

from models import Base
import connect_db
import models.users
import models.tickets
import models.orders
import models.products
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == '__main__':
    print('PyCharm')


connect_db.configurate_engine()
#Base.metadata.drop_all(bind=connect_db.engine)
Base.metadata.create_all(bind=connect_db.engine)

# Наполнение таблицы продукты
products = [['Блокнот', 20, 50], ['Блокнот цветной', 15, 0], ['Блокнот', 35, 45], ['Ручка', 100, 10],['Игральные кости', 10, 40]]
for product in products:
    try:
        models.products.creare_product(*product)
    except sqlalchemy.exc.IntegrityError:
        print(f'Позиция {product[0]} есть в БД')



while True:
    first_row = '===Добро пожаловать в "Не магазин" ==='
    second_row = 'Здесь вы можете обменивать тикеты для того, чтобы приобретать товары'
    third_row = 'Для взоимодействия используйте команды:'
    print(f'\t\t\t\t{first_row}\n{second_row}\n{third_row}\n')
    first_comand = '>\tТовары'
    second_comand = '>\tЗарегистрироваться'
    third_comand = '>\tВойти'
    print(f'{first_comand}\n{second_comand}\n{third_comand}')
    result = input('Введите команду:')
    if result == 'Товары':
        models.products.get_product()
    elif result == 'Зарегистрироваться':
        login_reg = input('Введите логин >')
        password_reg = input('Введите пароль >')
        if models.users.User.is_exist(login_reg):
            models.users.create_user(login_reg, password_reg)

    elif result == 'Войти':
        models.users.user_entry()
    else:
        break







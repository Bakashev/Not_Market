import connect_db
import models.tickets
import sqlalchemy.exc
from models import Base

# Наполнение таблицы продукты
products = [['Блокнот', 20, 50], ['Блокнот цветной', 15, 0], ['Блокнот', 35, 45], ['Ручка', 100, 10],['Игральные кости', 10, 40]]
for product in products:
    try:
        models.products.creare_product(*product)
    except sqlalchemy.exc.IntegrityError:
        print(f'Позиция {product[0]} есть в БД')

#Создание 1000 Tickets БД
models.tickets.Ticket.create_ticket()

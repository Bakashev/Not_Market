from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

import connect_db
from models import Base
from models import users
from models import products
from datetime import datetime

class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='order')
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship('Product', back_populates='order')
    count = Column(Integer)
    order_datetime = Column(DateTime)

#Покупка продукта
    @staticmethod
    def buy_product(number_id: int, count_: int):
        with connect_db.Session(autoflush=False, bind=connect_db.engine) as db:
            print(products.Product.get_cost(number_id) * count_)
            if users.User.balanse_user() < products.Product.get_cost(number_id) * count_:
                print('Недостаточно средств')
            else:
                order = Orders(user_id=users.user_id, product_id=number_id, count=count_, order_datetime=datetime.now())
                db.add(order)
                count = products.Product.get_count(number_id)
                db.commit()
                print(count)
                users.User.decrease_pointss(users.user_id, products.Product.get_cost(number_id) * count_)
                products.decrese_count(number_id, count_)
                print(f'Вы успешно купили {products.Product.get_name(number_id)} в количестве:'
                      f'{count_} \nУ вас осталась {users.User.balanse_user()}')


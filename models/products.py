from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from models import Base
import connect_db

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    cost = Column(Integer)
    count = Column(Integer)
    order = relationship('Orders', back_populates='product')



# Получение из католога количества по id продукта
    @staticmethod
    def get_count(id: int):
        with connect_db.Session(autoflush=False, bind=connect_db.engine) as db:
            res = db.query(Product).filter(Product.id == id)
            for element in res:
                return element.count

# Получение стоимости
    @staticmethod
    def get_cost(id: int):
        with connect_db.Session(autoflush=False, bind=connect_db.engine) as db:
            res = db.query(Product).filter(Product.id == id)
            for element in res:
                return element.cost

# Список продуктов
def get_product():
    with connect_db.Session(autoflush=False, bind=connect_db.engine) as db:
        res = db.query(Product).filter(Product.count > 0)
        name_list = ['ID', 'Стоимость', 'Кол-во', 'Название']
        for i in name_list:
            print(f'{i:<25}', end='')
        print()
        print('#' * 100)
        for element in res:
            print(f'{element.id:<25}{element.cost:<25}{element.count:<25}{element.name:<25}')
        # return res
# Создание записи в катологе
def creare_product(name:str, cost:int, count:int):
    #connect_db.configurate_engine()
    with connect_db.Session(autoflush=False, bind=connect_db.engine) as db:
        tmp = Product(name=name, cost=cost, count=count)
        db.add(tmp)
        db.commit()

# Уменьшение купленного товара
def decrese_count(id: int, count_: int):
    with connect_db.Session(autoflush=False, bind=connect_db.engine) as db:
        res = db.query(Product).filter(Product.id == id)
        for element in res:
            element.count -= count_
            db.commit()




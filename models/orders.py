from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models import Base

class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='order')
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship('Product', back_populates='order')
    count = Column(Integer)
    order_datetime = Column(DateTime)
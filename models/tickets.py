from sqlalchemy import Column, Boolean, Integer, String,  ForeignKey
from sqlalchemy.orm import relationship
from models import Base



class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)
    uuid = Column(String)
    available = Column(Boolean)
    user = Column(Integer, ForeignKey('users.id'))
    user_id = relationship('User', back_populates='ticket')

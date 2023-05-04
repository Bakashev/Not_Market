from sqlalchemy import Column, Boolean, Integer, String,  ForeignKey
from sqlalchemy.orm import relationship

import connect_db
from models import Base
import models.users

import uuid



class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)
    uuid = Column(String)
    available = Column(Boolean)
    user = Column(Integer, ForeignKey('users.id'))
    user_id = relationship('User', back_populates='ticket')

    @staticmethod
    def create_ticket():
        with connect_db.Session(autoflush=False, bind=connect_db.engine) as db:
            for _ in range(1000):
                ticket = str(uuid.uuid4())
                tmp = Ticket(uuid=ticket, available=True)
                db.add(tmp)
                db.commit()

    @staticmethod
    def use_ticket(uuid:str):
        with connect_db.Session(autoflush=False, bind=connect_db.engine) as db:
            res = db.query(Ticket).filter(Ticket.uuid==uuid)
            if res.count() == 0:
                print('Такого тикета не существует')
            else:
                for element in res:
                    if element.available:
                        element.available = False
                        element.user = models.users.user_id

                        models.users.User.update_points(element.user)
                        db.commit()

                    else:
                        print('Билет уже использован')




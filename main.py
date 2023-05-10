import menu
import connect_db
from models import Base
import models.users
import models.tickets
import models.orders
import models.products
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == '__main__':
    print('PyCharm')

connect_db.configurate_engine()


Base.metadata.drop_all(bind=connect_db.engine)
Base.metadata.create_all(bind=connect_db.engine)

menu.StartMenu.start_menu()






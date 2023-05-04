from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine

#pass 123
database = 'postgresql://postgres:123@localhost:5432/not_market'
engine = None
Session = sessionmaker(autoflush=False, bind=engine)


def configurate_engine():
    global engine
    if engine is None:
        engine = create_engine(database)
        Session.configure()

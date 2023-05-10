from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, ForeignKey, String
import connect_db


class Base(DeclarativeBase):
    pass



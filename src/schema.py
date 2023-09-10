from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, String, Text
import sqlite3

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    
    id = Column(name='id',
                type_=Integer(),
                primary_key=True,
                nullable=False,
                unique=True,
                autoincrement=True)
    
    username = Column(name="username",
                      type_=String(80))
    
    password = Column(name='password',
                      type_=Text())
    
engine = create_engine('sqlite:///database.db')


Base.metadata.create_all(engine)
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Text, ForeignKey

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    id_users = Column(Integer, primary_key=True)
    name = Column(Text, primary_key=True)


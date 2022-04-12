from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Text, ForeignKey

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    id_users = Column(Integer, nullable=False)
    name = Column(Text, nullable=False)
    positions = Column(Text, nullable=False)


class Staff_Rates(Base):
    __tablename__ = 'staff_rates'

    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=True)


class Motivational_Programs(Base):
    __tablename__ = 'motivational_programs'
    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=True)


class Career(Base):
    __tablename__ = 'career'
    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=True)
    img = Column(Text)


class Standards(Base):
    __tablename__ = 'standards'
    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=True)
    img = Column(Text)

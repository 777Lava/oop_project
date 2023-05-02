from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Time

Base = declarative_base()


class UserORM:
    tg_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False) 
    start_time = Column(Time, nullable=False)
    bus_station = Column(Integer, nullable=False)


class PassengerORM(Base, UserORM):
    __tablename__ = 'passengers'


class DriverORM(Base, UserORM):
    __tablename__ = 'drivers'

    places = Column(Integer, nullable=False)
    car = Column(String, nullable=False)

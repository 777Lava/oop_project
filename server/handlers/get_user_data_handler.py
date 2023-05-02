import os, sys

sys.path.append(fr'C:\Users\{os.getlogin()}\de_project')

from sqlalchemy.orm import Session
from sqlalchemy import select

from db import engine, DriverORM, PassengerORM
from server.shemas import Driver, Passenger
from typing import Union


async def get_user_data_handler(tg_id: int) -> Union[Driver, Passenger, bool]:
    with Session(engine) as db:
        q = select(DriverORM).where(DriverORM.tg_id == tg_id)
        driver_response = db.execute(q).fetchone()
    print(f'driver response: {driver_response}')
    if driver_response:
        return Driver.from_orm(driver_response[0])
    
    with Session(engine) as db:
        q = select(PassengerORM).where(PassengerORM.tg_id == tg_id)
        passenger_response = db.execute(q).fetchone()
    if passenger_response:
        return Passenger.from_orm(passenger_response[0])
    return False

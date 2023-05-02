import os, sys

sys.path.append(fr'C:\Users\{os.getlogin()}\de_project')

from sqlalchemy.orm import Session
from sqlalchemy import update, delete, and_

from db import engine, DriverORM, PassengerORM
from server.shemas import Driver, Passenger
from typing import Union


async def patch_user_handler(user: Union[Driver, Passenger]) -> bool:
    user_tg_id = user.tg_id
    new_params = user.dict()
    if "places" in user.dict():
        # class Driver detected
        q = update(DriverORM).where(DriverORM.tg_id == user_tg_id).values(new_params)
    else:
        # class Passenger detected
        q = update(PassengerORM).where(PassengerORM.tg_id == user_tg_id).values(new_params)

    # updating all user data except bus_stations
    with engine.connect() as db:
        db.execute(q)
        db.commit()
        db.close()
    
    return True

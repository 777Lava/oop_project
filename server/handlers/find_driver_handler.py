import os, sys

sys.path.append(fr'C:\Users\{os.getlogin()}\de_project')

from db import DriverORM
from server.shemas import Driver, Passenger
from . import get_user_data_handler

from typing import List, Optional
import datetime


async def find_driver_handler(passenger_tg_id: int, active_drivers: List[Driver]) -> Optional[Driver]:
    passenger = await get_user_data_handler(tg_id=passenger_tg_id)
    if not passenger:
        return None
    passenger_time = passenger.start_time
    passenger_timedelta = datetime.timedelta(hours=passenger_time.hour, minutes=passenger_time.minute)
    for driver in active_drivers:
        driver_time = driver.start_time
        driver_timedelta = datetime.timedelta(hours=driver_time.hour, minutes=driver_time.minute)
        if passenger.bus_station != driver.bus_station:
            continue
        if driver_timedelta > passenger_timedelta:
            if (driver_timedelta - passenger_timedelta).seconds // 60 > 10:
                continue
        else:
            if (passenger_timedelta - driver_timedelta).seconds // 60 > 10:
                continue
        active_drivers[driver] -= 1
        return driver
    return None
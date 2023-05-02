from pydantic import BaseModel, validator
from datetime import time, datetime
from typing import List


def string_to_time_encoder(date: str) -> time:
    print(datetime.strptime(date, "%H:%M").time())
    return datetime.strptime(date, "%H:%M").time()


class User(BaseModel):
    tg_id: int
    name: str
    start_time: time
    bus_station: int

    class Config:
        # json_encoders = {
        #     time: string_to_time_encoder
        # }
        orm_mode = True
        validate_assignment = True

    def __hash__(self) -> int:
        return hash((type(self),) + tuple(self.__dict__.values()))


class Driver(User):
    places: int
    car: str

    def __hash__(self) -> int:
        return super().__hash__()

class Passenger(User):
    pass

    def __hash__(self) -> int:
        return super().__hash__()

if __name__ == '__main__':
    dr = Driver(
        tg_id=1,
        name='asd',
        start_time=time(hour=1, minute=2),
        end_time=time(hour=1, minute=3),
        bus_station=1,
        places=1,
        car="asd 123"
    )
    a = dict()
    a[dr] = 1
    print(a[dr])

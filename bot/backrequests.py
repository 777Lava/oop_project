import os, sys

sys.path.append(fr'C:\Users\{os.getlogin()}\de_project')

import requests
import json

from server.shemas import Driver, Passenger

from typing import Union, Any

base_url = "http://127.0.0.1:8000/"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


def add_user(user: Union[Driver, Passenger]) -> bool:
    response = requests.post(url=base_url + 'user', data=json.dumps(user.dict(), default=str))
    response = json.loads(response.text)
    return response["msg"] == "success"


def get_user_from_db(tg_id: int) -> Union[Driver, Passenger, bool]:
    response = requests.get(url=base_url + "user", params={"tg_id": tg_id})
    response = json.loads(response.text)
    if "msg" in response:
        return False
    if "places" in response:
        return Driver(**response)
    return Passenger(**response)


def patch_user_from_db(user: Union[Driver, Passenger]) -> bool:
    response = requests.patch(url=base_url + 'user', data=json.dumps(user.dict(), default=str))
    response = json.loads(response.text)
    return response["msg"] == "success"


def add_driver_to_query(driver_tg_id: int) -> bool:
    response = requests.get(url=base_url + "add_driver_to_query", params={"driver_tg_id": driver_tg_id})
    response = json.loads(response.text)
    return response["msg"] == "success"


def find_driver_for_passenger(passenger_tg_id: int) -> Union[Driver, bool]:
    response = requests.get(url=base_url + "find_driver", params={"passenger_tg_id": passenger_tg_id})
    print(f'\n\n{response.text}\n\n')
    response = json.loads(response.text)
    if "msg" in response:
        return False
    return Driver(**response)


if __name__ == "__main__":

    psg = Passenger(tg_id=5,
                    name="asd",
                    start_time="07:30",
                    bus_station=1,
                    rating=2)
    drv = Driver(tg_id=1, 
                 name="asd asd",
                 start_time="07:35",
                 bus_station=1,
                 rating=5,
                 places=4,
                 car="213 asd")

    # print(add_user(psg))
    # print(add_user(drv))

    # print(get_user_from_db(5))
    print(add_driver_to_query(1))
    print(find_driver_for_passenger(5))
import pytest
import requests
from helpers import CreateCourier
from data import Urls, CreateOrder


@pytest.fixture()
def create_new_couirier():
    login_password = CreateCourier.register_new_courier_and_return_login_password()
    data = {"login": login_password[0], "password": login_password[1]}
    response = requests.post(Urls.URL + Urls.COUIRER, data)
    id_courier = response.json()["id"]
    yield id_courier
    requests.delete(Urls.URL + Urls.COUIRER + "/:" + str(id_courier))


@pytest.fixture()
def create_new_order():
    response = requests.post(url=Urls.URL + Urls.ORDER, json=CreateOrder.order_1)
    return response.json()["track"]

import allure
import pytest
import requests
from data import Urls, CreateOrder
from helpers import CreateCourier


class TestCreateOrder:

    @pytest.mark.parametrize(
        "body",
        [
            CreateOrder.order_1,
            CreateOrder.order_2,
            CreateOrder.order_3,
            CreateOrder.order_4
        ]
    )
    @allure.title('Успешное создание заказа')
    @allure.description("Проверка получения корректного кода и текста успешного создания заказа")
    def test_create_order_success(self, body):
        response = requests.post(url=Urls.URL + Urls.ORDER, json=body)
        assert response.status_code == 201 and "track" in response.text

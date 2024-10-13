import allure
import pytest
import requests
from data import Urls


class TestCreateOrder:
    @allure.title('Успешное получение списка заказов')
    @allure.description("Должны получить до 10-ти заказов")
    def test_get_list_order(self):
        response = requests.get(url=Urls.URL + Urls.ORDER + "?limit=10&page=0")
        assert response.status_code == 200

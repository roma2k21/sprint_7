import allure
import pytest
import requests
from data import Urls, LoginCourier
from helpers import CreateCourier


class TestLoginCourier:
    @allure.title('Успешная авторизация')
    @allure.description("Проверка успешной авторизации,статус кода и возврат id")
    def test_login_courier_success(self):
        login_password = CreateCourier.register_new_courier_and_return_login_password()
        payload = {"login": login_password[0], "password": login_password[1]}
        response = requests.post(Urls.URL + Urls.LOGIN_COUIRER, data=payload)
        assert response.status_code == 200 and "id" in response.text

    @pytest.mark.parametrize(
        "login, password",
        [
            LoginCourier.login_password_1,
            LoginCourier.login_password_2,
            LoginCourier.login_password_3
        ]
    )
    @allure.title('Попытка авторизации с пустым логином/паролем')
    @allure.description("Получение ошибки с пустыми данными для входа")
    def test_login_empty_data(self, login, password):
        data = {"login": login, "password": password}
        response = requests.post(Urls.URL + Urls.LOGIN_COUIRER, json=data)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Авторизация с несуществующим логином')
    @allure.description("Получение корректного кода и текста ошибки")
    def test_login_courier_wrong_login(self):
        data = {"login": "jinja100", "password": "1234"}
        response = requests.post(Urls.URL + Urls.LOGIN_COUIRER, json=data)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"

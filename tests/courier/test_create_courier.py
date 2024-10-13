import pytest
import allure
import requests
from data import Urls
from helpers import CreateCourier


class TestCreateCourier:
    @allure.title('Успешное создание курьера')
    @allure.description("Создание курьера, проверка кода и текста ответа")
    def test_create_courier_success(self):
        login = CreateCourier.generate_random_string(10)
        password = CreateCourier.generate_random_string(10)
        first_name = CreateCourier.generate_random_string(10)
        payload = {"login": login, "password": password, "first_name": first_name}
        response = requests.post(url=Urls.URL + Urls.COUIRER, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Повторное создание курьера')
    @allure.description("Создание курьера с существующим логином")
    def test_create_same_data_registration(self):
        login_password = CreateCourier.register_new_courier_and_return_login_password()
        payload = {"login": login_password[0], "password": login_password[1], "first_name": login_password[2]}
        response = requests.post(Urls.URL + Urls.COUIRER, data=payload)
        assert response.status_code == 409 and response.json()["message"] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Создание курьера с ошибкой в теле запроса')
    @allure.description("Запрос без логина")
    def test_create_courier_no_login(self):
        login_password = CreateCourier.register_new_courier_and_return_login_password()
        payload = {"password": login_password[1], "first_name": login_password[2]}
        response = requests.post(Urls.URL + Urls.COUIRER, data=payload)
        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Создание курьера с ошибкой в теле запроса')
    @allure.description("Запрос без пароля")
    def test_create_courier_no_password(self):
        login_password = CreateCourier.register_new_courier_and_return_login_password()
        payload = {"login": login_password[0], "first_name": login_password[2]}
        response = requests.post(Urls.URL + Urls.COUIRER, data=payload)
        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для создания учетной записи'

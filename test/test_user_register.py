import helpers
from helpers import RegisterUserWithoutDate
from burger_api import BurgerAPI
from data import Messages
import allure
import pytest


class TestCreateCourier:
    @allure.title('Проверка первичной регистрации пользователя с заполнением всех обязательных полей')
    def test_success_create_user(self, registered_user_payload):
        created_user = BurgerAPI.create_user(registered_user_payload)

        assert created_user.status_code == 200 and 'accessToken' in created_user.json() and created_user.json()['success'] == True

    @allure.title("Проверка повторной регистрации пользователя")
    def test_dublicat_create_user(self, get_new_data):
        created_user_1 = BurgerAPI.create_user(helpers.register_new_user_and_return_email_password(get_new_data))
        created_user_2 = created_user_1

        assert created_user_2.status_code == 403 and created_user_2.json()['message'] == Messages.ERROR_403_DUBLICATE

    @allure.title("Проверка регистрации пользователя без заполнения одного из полей")
    @pytest.mark.parametrize('email, password, name', [[None, RegisterUserWithoutDate.password, RegisterUserWithoutDate.name],
                                                       [RegisterUserWithoutDate.email, None, RegisterUserWithoutDate.name],
                                                       [RegisterUserWithoutDate.email, RegisterUserWithoutDate.password, None]])
    def test_create_user_without_some_date(self, email, password, name):
        payload = {
            "email": email,
            "name": name,
            "password": password
        }
        create_user = BurgerAPI.create_user(payload)

        assert create_user.status_code == 403 and create_user.json()['message'] == Messages.ERROR_403_WITHOUT_DATE
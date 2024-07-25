import pytest
import helpers
from burger_api import BurgerAPI


@pytest.fixture
def registered_user_payload():
    payload = helpers.get_user_registration_body()
    yield payload
    BurgerAPI.delete_user(payload)


@pytest.fixture
def get_new_data():
    payload = helpers.get_user_registration_body()
    yield payload

@pytest.fixture
def delete_user():
    BurgerAPI.delete_user()
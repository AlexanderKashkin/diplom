import os

import pytest

from api.resourses.user import UserModel
from api.resourses.user import auth
from utils import StatusCode
from utils.generator_random import generate_random_string
from dotenv import load_dotenv


@pytest.fixture
def user_data_for_register():
    """
    The first and last name must be unique
    """
    first_name = f'Ivan_{generate_random_string(4)}'
    last_name = f'Ivanov_{generate_random_string(4)}'
    password = '1234567'
    return UserModel(first_name=first_name, last_name=last_name, password=password)


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session')
def get_user_data_from_env():
    resp = auth(email=os.getenv('EMAIL'),
                password=os.getenv('PASSWORD'))
    assert resp.status_code == StatusCode.OK
    return UserModel(token=resp.json()['token'], _id=resp.json()['user']['_id'])

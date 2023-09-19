import pytest

import api.resourses as model
from utils.generator_random import generate_random_string


@pytest.fixture
def user_data_for_register():
    """
    The first and last name must be unique
    """
    first_name = f'Ivan_{generate_random_string(4)}'
    last_name = f'Ivanov_{generate_random_string(4)}'
    password = '1234567'
    return model.UserModel(first_name=first_name, last_name=last_name, password=password)

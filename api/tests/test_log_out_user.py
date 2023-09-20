import os

import allure
import pytest

from api.resourses.user import log_out, get_profile
from utils import Severity, StatusCode


@allure.severity(Severity.CRITICAL)
@allure.title('Проверка код ответа сервера после деавторизации')
@pytest.mark.api
def test_log_out(get_user_data_from_env):
    with allure.step('Осуществляем logout'):
        resp = log_out(token=get_user_data_from_env.token)
    with allure.step('Проверяем код ответа сервера'):
        assert resp.status_code == StatusCode.OK, f'{resp.status_code} is not {StatusCode.OK}'


@allure.severity(Severity.CRITICAL)
@allure.title('Проверка получения данных пользователя, для которого выполнена деавторизация')
@pytest.mark.api
def test_log_out_and_get_user_data(get_user_data_from_env):
    token = get_user_data_from_env.token
    with allure.step('Осуществляем logout'):
        log_out(token=token)
    with allure.step('Получаем данные пользователя с истекшим токеном'):
        assert get_profile(token).status_code == StatusCode.UNAUTHORIZED, (f'{get_profile(token).status_code}'
                                                                           f'is not {StatusCode.UNAUTHORIZED}')
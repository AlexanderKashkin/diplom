import json

import allure
import pytest
from jsonschema.validators import validate

from api.resourses.contact import put_contact
from api.resourses.json_schema import contact_json_path
from utils.handbook import Severity, StatusCode


@allure.severity(Severity.BLOCKER)
@allure.title('Валидация кода и ответа сервера после частичной замены данных контакта')
@pytest.mark.api
@pytest.mark.contact
def test_partial_replacement_contact(get_user_data_from_env, add_contact_fixture):
    last_name = 'new_last_name'
    obj_last_name = {'lastName': last_name}
    with allure.step('Заменяем поле last_name для контакта'):
        resp = put_contact(get_user_data_from_env.token, add_contact_fixture.json()['_id'], obj_last_name)
    with allure.step('Валидируем код ответа сервера'):
        assert resp.status_code == StatusCode.OK
    with allure.step('Проверяем, что поле было заменено'):
        assert resp.json()['lastName'] == last_name


# test flaky

@allure.severity(Severity.CRITICAL)
@allure.title('Валидация JSON_SCHEMA после частичной замены данных контакта')
@pytest.mark.api
@pytest.mark.contact
def test_partial_replacement_contact_validate_json_schema(get_user_data_from_env, add_contact_fixture):
    with allure.step('Читаем файл-образец с json_schema'):
        with open(contact_json_path) as file:
            schema = json.loads(file.read())
    last_name = 'new_last_name'
    obj_last_name = {'lastName': last_name}
    with allure.step('Заменяем поле last_name для контакта'):
        resp = put_contact(get_user_data_from_env.token, add_contact_fixture.json()['_id'], obj_last_name)
    with allure.step('Валидация JSON_SCHEMA после частичной замены данных контакта'):
        validate(resp.json(), schema)
# test flaky

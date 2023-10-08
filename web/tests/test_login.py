import allure
import pytest

from utils import Severity
from web.resourses import Login, Logout


@allure.severity(Severity.BLOCKER)
@allure.title('Авторизация пользователя')
@pytest.mark.web
def test_login(web_user_for_auth):
    page = Login(web_user_for_auth)
    page.open()
    page.fill_form()
    page.submit()
    page.check_result_after_login(header='Contact List', sub_header='Click on any contact to view the Contact Details')


@allure.severity(Severity.BLOCKER)
@allure.title('Деавторизация пользователя')
@pytest.mark.web
def test_logout(web_user_for_auth):
    login_page = Login(web_user_for_auth)
    login_page.open()
    login_page.fill_form()
    login_page.submit()
    logout_page = Logout()
    logout_page.log_out()
    logout_page.check_result_after_log_out(
        header='Contact List App',
        sub_header='Welcome! This application is for testing purposes only. '
                   'The database will be purged as needed to keep costs down.',
        href='here'
    )

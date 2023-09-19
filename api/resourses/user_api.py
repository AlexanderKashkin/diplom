import requests
from .user_model import UserModel
from .user_view import UserView
from utils import BASE_URL, Method, do_request


class UserApi:
    def __init__(self) -> None:
        self.base_url = BASE_URL
        self.endpoint = '/users'

    def registration(self, first_name: str, last_name: str, password: str) -> requests:
        data = UserView(UserModel(first_name=first_name, last_name=last_name, password=password)).full()
        resp = do_request(
            method=Method.POST,
            base_url=self.base_url,
            url=f'{self.endpoint}',
            json=data
        )
        return resp

    def log_in(self, email: str, password: str) -> requests:
        resp = do_request(
            method=Method.POST,
            base_url=self.base_url,
            url=f'{self.endpoint}/login',
            data=UserView(UserModel(email, password)).for_auth()

        )
        return resp

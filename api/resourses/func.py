import requests

from .user_api import UserApi


def register(first_name: str, last_name: str, password: str) -> requests:
    return UserApi().registration(first_name, last_name, password)


def auth(email: str, password: str) -> requests:
    return UserApi().log_in(email, password)

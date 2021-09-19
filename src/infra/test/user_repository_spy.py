from typing import Union, List
from src.domain.models import Users
from src.domain.test.mock_users import mock_users


class UserRepositorySpy:

    def __init__(self) -> None:
        self.insert_user_params: dict = {}
        self.select_user_params: dict = {}

    def insert_user(self, name: str, password: str) -> Users:
        self.insert_user_params['name'] = name
        self.insert_user_params['password'] = password

        return mock_users()

    def select_user(self, user_id: int = None, name: str = None) -> Union[List[Users], None]:
        self.select_user_params['user_id'] = user_id
        self.select_user_params['name'] = name

        return [mock_users()]

from abc import ABC, abstractmethod
from typing import List, Union
from src.domain.models import Users


class UserRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(self, name: str, password: str) -> Users:
        raise Exception("Method not implemented")

    @abstractmethod
    def select_user(self, user_id: int = None, name: str = None) -> Union[List[Users], None]:
        raise Exception("Method not implemented")

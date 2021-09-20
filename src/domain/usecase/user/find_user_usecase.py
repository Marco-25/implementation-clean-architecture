from abc import ABC, abstractmethod


class FindUserInterface(ABC):

    @abstractmethod
    def find_user_by_id(self, user_id: int) -> dict:
        raise Exception("Method not implementation: find_user_by_id")

    @abstractmethod
    def find_user_by_name(self, name: str) -> dict:
        raise Exception("Method not implementation: find_user_by_name")

    @abstractmethod
    def find_user_by_id_and_name(self, user_id: int, name: str) -> dict:
        raise Exception("Method not implementation: find_user_by_id_and_name")

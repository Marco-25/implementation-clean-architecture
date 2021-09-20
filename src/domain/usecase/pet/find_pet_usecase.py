from abc import ABC, abstractmethod


class FindPetInterface(ABC):

    @abstractmethod
    def find_pet_by_id(self, pet_id: int) -> dict:
        raise Exception("Method not implementation: find_pet_by_id")

    @abstractmethod
    def find_pet_by_user_id(self, user_id: int) -> dict:
        raise Exception("Method not implementation: find_pet_by_user_id")

    @abstractmethod
    def find_pet_by_id_and_user_id(self, pet_id: int, user_id: int) -> dict:
        raise Exception("Method not implementation: find_pet_by_id_and_name")

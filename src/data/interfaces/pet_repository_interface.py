from abc import ABC, abstractmethod
from typing import List, Union
from src.domain.models import Pets


class PetRepositoryInterface(ABC):

    @abstractmethod
    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        raise Exception("Method not implemented")

    @abstractmethod
    def select_pet(self, user_id: int = None, pet_id: int = None) -> Union[List[Pets], None]:
        raise Exception("Method not implemented")

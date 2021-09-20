from abc import ABC, abstractmethod


class RegisterPetInterface(ABC):

    @abstractmethod
    def register_pet(self, name: str, specie: str, user: dict, age: int = None) -> dict:
        raise Exception("Method not implemented: register_pet")

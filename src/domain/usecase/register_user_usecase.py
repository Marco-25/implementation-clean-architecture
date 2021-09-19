from abc import ABC, abstractmethod


class RegisterUserInterface(ABC):

    @abstractmethod
    def register(self, name: str, password: str) -> dict:
        raise Exception("Method not implementation: register")

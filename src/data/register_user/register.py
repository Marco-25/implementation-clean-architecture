from src.domain.usecase.register_user_usecase import RegisterUserInterface
from src.data.interfaces.user_repository_interface import UserRepositoryInterface as UserRepository


class RegisterUser(RegisterUserInterface):

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, name: str, password: str) -> dict:

        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = self.user_repository.insert_user(name, password)

        return {"success": validate_entry, "Users": response}

from src.data.interfaces.user_repository_interface import UserRepositoryInterface as UserRepository
from src.domain.usecase.user.find_user_usecase import FindUserInterface


class FindUser(FindUserInterface):

    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def find_user_by_id(self, user_id: int) -> dict:

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id)

        return {"success": validate_entry, "Users": response}

    def find_user_by_name(self, name: str) -> dict:
        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.user_repository.select_user(name=name)

        return {"success": validate_entry, "Users": response}

    def find_user_by_id_and_name(self, user_id: int, name: str) -> dict:
        response = None
        validate_entry = isinstance(user_id, int) and isinstance(name, str)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id, name=name)

        return {"success": validate_entry, "Users": response}

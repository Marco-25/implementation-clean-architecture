from src.domain.usecase.pet.register_pet_usecase import RegisterPetInterface
from src.data.interfaces.pet_repository_interface import PetRepositoryInterface
from src.data.user.find_user import FindUser


class RegisterPet(RegisterPetInterface):

    def __init__(self, pet_repository: PetRepositoryInterface, find_user: FindUser) -> None:
        self.pet_repository = pet_repository
        self.find_user = find_user

    def register_pet(self, name: str, specie: str, user: dict, age: int = None) -> dict:

        response = None
        validate_entry = isinstance(name, str) and isinstance(specie, str)
        validate_user = self.__find_user(user)

        checked_user = validate_entry and validate_user['success']

        if checked_user:
            response = self.pet_repository.insert_pet(name, specie, age, user["user_id"])

        return {"success": checked_user, "Pets": response}

    def __find_user(self, user: dict) -> dict:

        search_user = None

        if user["user_id"] and user["user_name"]:
            search_user = self.find_user.find_user_by_id_and_name(user["user_id"], user["user_name"])

        elif user["user_id"] and not user["user_name"]:
            search_user = self.find_user.find_user_by_id(user["user_id"])

        elif not user["user_id"] and user["user_name"]:
            search_user = self.find_user.find_user_by_name(user["user_name"])

        else:
            return {"success": False, "Users": None}

        return search_user

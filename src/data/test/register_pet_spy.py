from src.domain.test import mock_pets, mock_users


class RegisterPetSpy:

    def __init__(self, pet_repository, find_user) -> None:
        self.pet_repository = pet_repository
        self.find_user = find_user
        self.register_pet_param: dict = {}

    def register_pet(self, name: str, specie: str, user: dict, age: int = None) -> dict:

        self.register_pet_param["name"] = name
        self.register_pet_param["specie"] = specie
        self.register_pet_param["user"] = user
        self.register_pet_param["age"] = age

        response = None
        validate_entry = isinstance(name, str) and isinstance(specie, str)
        validate_user = self.__find_user(user)

        checked_user = validate_entry and validate_user['success']

        if checked_user:
            response = mock_pets()

        return {"success": checked_user, "Pets": response}

    def __find_user(self, user: dict) -> dict:

        search_user = None

        if user["user_id"] and user["user_name"]:
            search_user = {"success": True, "Users": mock_users()}

        elif user["user_id"] and not user["user_name"]:
            search_user = {"success": True, "Users": mock_users()}

        elif not user["user_id"] and user["user_name"]:
            search_user = {"success": True, "Users": mock_users()}

        else:
            return {"success": False, "Users": None}

        return search_user

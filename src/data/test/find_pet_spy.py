from src.domain.test import mock_pets


class FindPetSpy:

    def __init__(self, pet_repository):
        self.pet_repository = pet_repository
        self.by_pet_id_param: dict = {}
        self.by_user_id_param: dict = {}
        self.by_pet_id_and_user_id_param: dict = {}

    def find_pet_by_id(self, pet_id: int) -> dict:

        self.by_pet_id_param["pet_id"] = pet_id
        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = [mock_pets()]

        return {"success": validate_entry, "Pets": response}

    def find_pet_by_user_id(self, user_id: int) -> dict:

        self.by_user_id_param["user_id"] = user_id
        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = [mock_pets()]

        return {"success": validate_entry, "Pets": response}

    def find_pet_by_id_and_user_id(
        self, pet_id: int, user_id: int
    ) -> dict:

        self.by_pet_id_and_user_id_param["pet_id"] = pet_id
        self.by_pet_id_and_user_id_param["user_id"] = user_id
        response = None
        validate_entry = isinstance(user_id, int) and isinstance(pet_id, int)

        if validate_entry:
            response = [mock_pets()]

        return {"success": validate_entry, "Pets": response}

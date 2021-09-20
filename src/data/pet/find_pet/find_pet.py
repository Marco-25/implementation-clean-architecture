from src.data.interfaces.pet_repository_interface import PetRepositoryInterface
from src.domain.usecase.user.find_pet_usecase import FindPetInterface


class FindPet(FindPetInterface):

    def __init__(self, pet_repository: PetRepositoryInterface) -> None:
        self.pet_repository = pet_repository

    def find_pet_by_id(self, pet_id: int) -> dict:

        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id)

        return {"success": validate_entry, "Pets": response}

    def find_pet_by_user_id(self, user_id: int) -> dict:
        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(user_id=user_id)

        return {"success": validate_entry, "Pets": response}

    def find_pet_by_id_and_user_id(self, pet_id: int, user_id: int) -> dict:
        response = None
        validate_entry = isinstance(pet_id, int) and isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id, user_id=user_id)

        return {"success": validate_entry, "Pets": response}

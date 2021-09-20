from faker import Faker
from .find_pet import FindPet
from src.infra.test import PetRepositorySpy

faker = Faker()


def test_find_pet_by_id():
    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {"id": faker.random_number(digits=2)}
    response = find_pet.find_pet_by_id(attributes['id'])

    # testing inputs
    assert pet_repository.select_pet_params['pet_id'] == attributes['id']

    # testing outputs
    assert response['success'] is True
    assert response is not None


def test_find_pet_by_id_fail():
    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {"id": faker.name()}
    response = find_pet.find_pet_by_id(attributes['id'])

    # testing inputs
    assert pet_repository.select_pet_params == {}

    # testing outputs
    assert response['success'] is False
    assert response["Pets"] is None


def test_find_pet_by_user_id():
    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {"user_id": faker.random_number(digits=2)}
    response = find_pet.find_pet_by_user_id(attributes['user_id'])

    # testing inputs
    assert pet_repository.select_pet_params['user_id'] == attributes['user_id']

    # testing outputs
    assert response['success'] is True
    assert response is not None


def test_find_pet_by_user_id_fail():
    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {"user_id": faker.name()}
    response = find_pet.find_pet_by_user_id(attributes['user_id'])

    # testing inputs
    assert pet_repository.select_pet_params == {}

    # testing outputs
    assert response['success'] is False
    assert response["Pets"] is None


def test_find_pet_by_id_and_user_id():
    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {
        "id": faker.random_number(digits=2),
        "user_id": faker.random_number(digits=2)
    }
    response = find_pet.find_pet_by_id_and_user_id(attributes['id'], attributes['user_id'])

    # testing inputs
    assert pet_repository.select_pet_params['pet_id'] == attributes['id']
    assert pet_repository.select_pet_params['user_id'] == attributes['user_id']

    # testing outputs
    assert response['success'] is True
    assert response is not None


def test_find_pet_by_id_and_name_fail():
    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {
        "id": faker.name(),
        "user_id": faker.name()
    }
    response = find_pet.find_pet_by_id_and_user_id(attributes['id'], attributes['user_id'])

    # testing inputs
    assert pet_repository.select_pet_params == {}

    # testing outputs
    assert response['success'] is False
    assert response['Pets'] is None

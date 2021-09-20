from faker import Faker
from src.infra.test import PetRepositorySpy, UserRepositorySpy
from src.data.test import FindUserSpy
from.register import RegisterPet

faker = Faker()


def test_regiter():

    pet_repository = PetRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())

    register_pet = RegisterPet(pet_repository, find_user)

    attributes = {
        "name": faker.name(),
        "specie": "dog",
        "age": faker.random_number(digits=1),
        "user": {
            "user_id": faker.random_number(digits=5),
            "user_name": faker.name()
        }
    }

    response = register_pet.register_pet(
        name=attributes["name"],
        specie=attributes["specie"],
        user=attributes["user"],
        age=attributes["age"]
    )

    # testing inputs
    assert pet_repository.insert_pet_params["name"] == attributes["name"]
    assert pet_repository.insert_pet_params["specie"] == attributes["specie"]
    assert pet_repository.insert_pet_params["age"] == attributes["age"]

    # testing inputs find_users
    assert find_user.find_user_by_id_and_name_param['user_id'] == attributes['user']["user_id"]
    assert find_user.find_user_by_id_and_name_param['name'] == attributes['user']["user_name"]

    # testing outputs
    assert response['success'] is True
    assert response['Pets'] is not None


def test_regiter_fail():

    pet_repository = PetRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())

    register_pet = RegisterPet(pet_repository, find_user)

    attributes = {
        "name": faker.name(),
        "specie": "dog",
        "age": faker.random_number(digits=1),
        "user": {
            "user_id": faker.name(),
            "user_name": faker.random_number(digits=5)
        }
    }

    response = register_pet.register_pet(
        name=attributes["name"],
        specie=attributes["specie"],
        user=attributes["user"],
        age=attributes["age"]
    )

    # testing inputs
    assert pet_repository.insert_pet_params == {}

    # testing inputs find_users
    assert find_user.find_user_by_id_and_name_param['user_id'] == attributes['user']["user_id"]
    assert find_user.find_user_by_id_and_name_param['name'] == attributes['user']["user_name"]

    # testing outputs
    assert response['success'] is False
    assert response['Pets'] is None

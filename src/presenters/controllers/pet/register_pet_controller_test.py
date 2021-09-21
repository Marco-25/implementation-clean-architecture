from faker import Faker
from .register_pet_controller import RegisterPetController
from src.data.test import RegisterPetSpy
from src.infra.test import PetRepositorySpy, UserRepositorySpy
from src.presenters.helpers import HttpRequest

faker = Faker()


def test_route():

    register_pet_usecase = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_controller = RegisterPetController(register_pet_usecase)

    attributes = {
        "name": faker.name(),
        "specie": "dog",
        "age": faker.random_number(digits=1),
        "user": {
            "user_id": faker.random_number(digits=1),
            "user_name": faker.word()
        }
    }

    response = register_pet_controller.route(HttpRequest(body=attributes))

    # testing inputs
    assert register_pet_usecase.register_pet_param["name"] == attributes['name']
    assert register_pet_usecase.register_pet_param["specie"] == attributes['specie']
    assert register_pet_usecase.register_pet_param["age"] == attributes['age']
    assert register_pet_usecase.register_pet_param["user"] == attributes['user']

    # testing output
    assert response.status_code == 200
    assert "error" not in response.body

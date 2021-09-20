from faker import Faker
from src.infra.test.user_repository_spy import UserRepositorySpy
from.register import RegisterUser

faker = Faker()


def test_regiter():

    user_repository = UserRepositorySpy()
    register_user = RegisterUser(user_repository)

    attributes = {
        "name": faker.name(),
        "password": faker.word()
    }

    response = register_user.register(attributes['name'], attributes['password'])

    # testing inputs
    assert user_repository.insert_user_params['name'] == attributes['name']
    assert user_repository.insert_user_params['password'] == attributes['password']

    # testing outputs
    assert response["success"] is True
    assert response["Users"] is not None


def test_regiter_fail():

    user_repository = UserRepositorySpy()
    register_user = RegisterUser(user_repository)

    attributes = {
        "name": faker.name(),
        "password": faker.random_number()
    }

    response = register_user.register(attributes['name'], attributes['password'])

    # testing inputs
    assert user_repository.insert_user_params == {}

    # testing outputs
    assert response["success"] is False
    assert response["Users"] is None

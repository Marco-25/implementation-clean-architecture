from faker import Faker
from .find_user import FindUser
from src.infra.test import UserRepositorySpy as UserRepository

faker = Faker()


def test_find_user_by_id():
    user_repository = UserRepository()
    find_user = FindUser(user_repository)

    attributes = {"id": faker.random_number(digits=2)}
    response = find_user.find_user_by_id(attributes['id'])

    # testing inputs
    assert user_repository.select_user_params['user_id'] == attributes['id']

    # testing outputs
    assert response['success'] is True
    assert response is not None


def test_find_user_by_id_fail():
    user_repository = UserRepository()
    find_user = FindUser(user_repository)

    attributes = {"id": faker.name()}
    response = find_user.find_user_by_id(attributes['id'])

    # testing inputs
    assert user_repository.select_user_params == {}

    # testing outputs
    assert response['success'] is False
    assert response["Users"] is None


def test_find_user_by_name():
    user_repository = UserRepository()
    find_user = FindUser(user_repository)

    attributes = {"name": faker.name()}
    response = find_user.find_user_by_name(attributes['name'])

    # testing inputs
    assert user_repository.select_user_params['name'] == attributes['name']

    # testing outputs
    assert response['success'] is True
    assert response is not None


def test_find_user_by_name_fail():
    user_repository = UserRepository()
    find_user = FindUser(user_repository)

    attributes = {"name": faker.random_number()}
    response = find_user.find_user_by_name(attributes['name'])

    # testing inputs
    assert user_repository.select_user_params == {}

    # testing outputs
    assert response['success'] is False
    assert response["Users"] is None


def test_find_user_by_id_and_name():
    user_repository = UserRepository()
    find_user = FindUser(user_repository)

    attributes = {
        "id": faker.random_number(digits=2),
        "name": faker.name()
    }
    response = find_user.find_user_by_id_and_name(attributes['id'], attributes['name'])

    # testing inputs
    assert user_repository.select_user_params['user_id'] == attributes['id']
    assert user_repository.select_user_params['name'] == attributes['name']

    # testing outputs
    assert response['success'] is True
    assert response is not None


def test_find_user_by_id_and_name_fail():
    user_repository = UserRepository()
    find_user = FindUser(user_repository)

    attributes = {
        "id": faker.name(),
        "name": faker.random_number()
    }
    response = find_user.find_user_by_id_and_name(attributes['id'], attributes['name'])

    # testing inputs
    assert user_repository.select_user_params == {}

    # testing outputs
    assert response['success'] is False
    assert response['Users'] is None

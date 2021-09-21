from faker import Faker
from .find_user import FindUserController
from src.data.test import FindUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest

faker = Faker()


def test_handle():

    user_repository = UserRepositorySpy()
    find_user_usecase = FindUserSpy(user_repository)

    find_user_controller = FindUserController(find_user_usecase)

    http_request = HttpRequest(
        query={"user_id": faker.random_number(), "user_name": faker.name()}
    )

    response = find_user_controller.handle(http_request)

    # testing inputs
    assert find_user_usecase.find_user_by_id_and_name_param["user_id"] == http_request.query["user_id"]
    assert find_user_usecase.find_user_by_id_and_name_param["name"] == http_request.query["user_name"]

    # testing outputs
    assert response.status_code == 200
    assert response.body is not None


def test_handle_no_query_params():

    user_repository = UserRepositorySpy()
    find_user_usecase = FindUserSpy(user_repository)

    find_user_controller = FindUserController(find_user_usecase)

    http_request = HttpRequest()

    response = find_user_controller.handle(http_request)

    # testing inputs
    assert find_user_usecase.find_user_by_id_and_name_param == {}
    assert find_user_usecase.find_user_by_id_param == {}
    assert find_user_usecase.find_user_by_name_param == {}

    # testing outputs
    assert response.status_code == 400
    assert "error" in response.body

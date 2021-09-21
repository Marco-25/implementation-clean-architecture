from src.domain.usecase.user import RegisterUserInterface as RegisterUser
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class RegisterUserController():

    def __init__(self, register_user_use_case: RegisterUser):
        self.register_user_use_case = register_user_use_case

    def route(self, http_request: HttpRequest) -> HttpResponse:

        response = None

        if http_request.body:

            body_params = http_request.body.keys()

            if "name" in body_params and "password" in body_params:
                name = http_request.body["name"]
                password = http_request.body["password"]
                response = self.register_user_use_case.register(
                    name=name, password=password
                )

            else:
                response = {"success": False, "Users": None}

            if response["success"] is False:
                https_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Users"])

        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )

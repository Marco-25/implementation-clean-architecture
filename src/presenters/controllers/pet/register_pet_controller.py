from typing import Union, Dict
from src.domain.usecase.pet import RegisterPetInterface
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class RegisterPetController():

    def __init__(self, register_pet_usecase: RegisterPetInterface) -> None:
        self.register_pet_usecase = register_pet_usecase

    def route(self, http_request: HttpRequest) -> Union[HttpResponse, Dict]:

        response = None
        if http_request.body:

            body_params = http_request.body.keys()

            if "name" in body_params and "specie" in body_params and "user" in body_params:

                user_details = http_request.body['user'].keys()

                if "user_id" in user_details or "user_name" in user_details:

                    name = http_request.body["name"]
                    specie = http_request.body["specie"]
                    user = http_request.body["user"]

                    if "age" in body_params:
                        age = http_request.body["age"]
                    else:
                        age = None

                    response = self.register_pet_usecase.register_pet(
                        name=name,
                        specie=specie,
                        user=user,
                        age=age
                    )

                else:
                    response = {"success": False, "Pets": None}

            else:
                response = {"success": False, "Pets": None}

            if response["success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"],
                    body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Pets"])

        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"],
            body=http_error["body"]
        )

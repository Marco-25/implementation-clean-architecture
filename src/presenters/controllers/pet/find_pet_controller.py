from src.domain.usecase.pet import FindPetInterface as FindPet
from src.presenters.helpers import HttpResponse, HttpRequest
from src.presenters.errors import HttpErrors


class FindPetController:

    def __init__(self, find_pet_use_case: FindPet):
        self.find_pet_use_case = find_pet_use_case

    def route(self, http_request: HttpRequest) -> HttpResponse:

        response = None

        if http_request.query:

            query_string_params = http_request.query.keys()

            if "pet_id" in query_string_params and "user_id" in query_string_params:
                pet_id = http_request.query["pet_id"]
                user_id = http_request.query["user_id"]
                response = self.find_pet_use_case.find_pet_by_id_and_user_id(
                    pet_id=pet_id, user_id=user_id
                )

            elif (
                "pet_id" in query_string_params and "user_id" not in query_string_params
            ):
                pet_id = http_request.query["pet_id"]
                response = self.find_pet_use_case.find_pet_by_id(pet_id=pet_id)

            elif (
                "user_id" in query_string_params and "pet_id" not in query_string_params
            ):
                user_id = http_request.query["user_id"]
                response = self.find_pet_use_case.find_pet_by_user_id(user_id=user_id)

            else:
                response = {"success": False, "Pets": None}

            if response["success"] is False:
                https_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Pets"])

        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )

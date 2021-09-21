from src.domain.usecase.user.find_user_usecase import FindUserInterface as FindUser
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class FindUserController():

    def __init__(self, find_user_usecase: FindUser) -> None:
        self.find_user_usecase = find_user_usecase

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        response = None

        if http_request.query:

            if http_request.query["user_id"] and http_request.query["user_name"]:
                user_id = http_request.query["user_id"]
                user_name = http_request.query["user_name"]
                response = self.find_user_usecase.find_user_by_id_and_name(user_id=user_id, name=user_name)

            elif http_request.query["user_id"] and not http_request.query["user_name"]:
                user_id = http_request.query["user_id"]
                response = self.find_user_usecase.find_user_by_id(user_id=user_id)

            elif not http_request.query["user_id"] and http_request.query["user_name"]:
                user_id = http_request.query["user_name"]
                response = self.find_user_usecase.find_user_by_name(name=user_name)

            else:
                return HttpResponse(
                    status_code=404,
                    body=None
                )

            if response["success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error['status_code'],
                    body=http_error['body']
                )

            return HttpResponse(
                status_code=200,
                body=response["Users"]
            )

        http_error = HttpErrors.error_400()
        return HttpResponse(status_code=http_error['status_code'], body=http_error['body'])

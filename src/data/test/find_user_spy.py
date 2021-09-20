from src.domain.test import mock_users


class FindUserSpy:

    def __init__(self, user_repository) -> None:
        self.user_repository = user_repository
        self.find_user_by_id_param: dict = {}
        self.find_user_by_name_param: dict = {}
        self.find_user_by_id_and_name_param: dict = {}

    def find_user_by_id(self, user_id: int) -> dict:

        self.find_user_by_id_param["user_id"] = user_id
        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = [mock_users()]

        return {"success": validate_entry, "Users": response}

    def find_user_by_name(self, name: str) -> dict:

        self.find_user_by_name_param["name"] = name
        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = [mock_users()]

        return {"success": validate_entry, "Users": response}

    def find_user_by_id_and_name(self, user_id: int, name: str) -> dict:

        self.find_user_by_id_and_name_param["user_id"] = user_id
        self.find_user_by_id_and_name_param["name"] = name
        response = None
        validate_entry = isinstance(name, str) and isinstance(user_id, int)

        if validate_entry:
            response = [mock_users()]

        return {"success": validate_entry, "Users": response}

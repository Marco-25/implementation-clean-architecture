from src.domain.test import mock_users


class RegisterUserSpy:

    def __init__(self, user_repository):
        self.user_repository = user_repository
        self.register_param: dict = {}

    def register(self, name: str, password: str) -> dict:

        self.register_param["name"] = name
        self.register_param["password"] = password

        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = mock_users()

        return {"success": validate_entry, "Users": response}

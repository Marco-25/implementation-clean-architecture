from src.domain.models import Users
from src.infra.SqLite.config import DBConnectionHandler
from src.infra.SqLite.entities import Users as UsersModel


class UserRepository:

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:

        with DBConnectionHandler() as db_connection:
            try:
                new_user = UsersModel(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
                return Users(new_user.id, new_user.name, new_user.password)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

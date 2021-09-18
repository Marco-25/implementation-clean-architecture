
from src.infra.SqLite.config import DBConnectionHandler
from src.infra.SqLite.entities import Users


class UserRepository:

    @classmethod
    def insert_user(cls, name: str, password: str) -> dict:

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
                db_connection.session.refresh(new_user)
                return new_user.to_json()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

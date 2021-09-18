from typing import List, Union
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

    @classmethod
    def select_user(cls, user_id: int = None, name: str = None) -> Union[List[Users], None]:

        try:
            query = None

            if user_id and not name:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(UsersModel).filter_by(id=user_id).first()
                    query = [data]

            if not user_id and name:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(UsersModel).filter_by(name=name).first()
                    query = [data]

            if user_id and name:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(UsersModel).filter_by(id=user_id, name=name).first()
                    query = [data]

            return query
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

        return None

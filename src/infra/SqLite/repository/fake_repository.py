from src.infra.SqLite.config import DBConnectionHandler
from src.infra.SqLite.entities import Users


class FakeRepository:

    @classmethod
    def insert_user(cls, name: str, password: str):

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Marco", password="123456")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

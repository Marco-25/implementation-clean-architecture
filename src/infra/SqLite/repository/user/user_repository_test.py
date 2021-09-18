from faker import Faker
from src.infra.SqLite.config import DBConnectionHandler
from src.infra.SqLite.repository.user.user_repository import UserRepository

faker = Faker()
user_repository = UserRepository()
db_connect = DBConnectionHandler()


def test_insert_user():
    """ Should insert User """
    name = faker.name()
    password = faker.word()
    engine = db_connect.get_engine()

    new_user = user_repository.insert_user(name, password)
    query_user = engine.execute("SELECT * FROM users WHERE id={}".format(new_user['id'])).fetchone()

    engine.execute("DELETE FROM users WHERE id={}".format(new_user['id']))

    assert new_user['id'] == 10
    assert new_user['name'] == query_user.name
    assert new_user['password'] == query_user.password

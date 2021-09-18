from faker import Faker
from src.infra.SqLite.config import DBConnectionHandler
from src.infra.SqLite.repository.user.user_repository import UserRepository
from src.infra.SqLite.entities import Users

faker = Faker()
user_repository = UserRepository()
db_connect = DBConnectionHandler()


def test_insert_user():
    """ Should insert User """
    name = faker.name()
    password = faker.word()
    engine = db_connect.get_engine()

    new_user = user_repository.insert_user(name, password)
    query_user = engine.execute("SELECT * FROM users WHERE id={}".format(new_user.id)).fetchone()

    engine.execute("DELETE FROM users WHERE id={}".format(new_user.id))

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password


def test_select_user():
    """ Should select a user in Users table and compare it """
    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.word()

    data = Users(id=user_id, name=name, password=password)

    engine = db_connect.get_engine()
    engine.execute(
        "INSERT INTO users (id, name, password) VALUES ('{}', '{}', '{}');".format(user_id, name, password)
    )

    query_select1 = user_repository.select_user(user_id=user_id)
    query_select2 = user_repository.select_user(name=name)
    query_select3 = user_repository.select_user(user_id=user_id, name=name)

    assert data in query_select1
    assert data in query_select2
    assert data in query_select3

    engine.execute(
        "DELETE FROM users WHERE id={}".format(user_id)
    )

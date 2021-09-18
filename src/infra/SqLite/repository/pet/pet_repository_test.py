from faker import Faker
from src.infra.SqLite.repository.pet.pet_repository import PetRepository
from src.infra.SqLite.config import DBConnectionHandler
from src.infra.SqLite.entities.pets import AnimalTypes
from src.infra.SqLite.entities import Pets

faker = Faker()
pet_repository = PetRepository()
db_connect = DBConnectionHandler()


def test_insert_pet():
    """ Should select a pet in Pets table and compare it """

    name = faker.name()
    specie = "dog"
    age = faker.random_number(digits=2)
    user_id = faker.random_number(digits=5)

    new_pet = pet_repository.insert_pet(name, specie, age, user_id)

    engine = db_connect.get_engine()
    query_pet = engine.execute("SELECT * FROM pets WHERE id={}".format(new_pet.id)).fetchone()

    assert new_pet.id == query_pet.id
    assert new_pet.name == query_pet.name
    assert new_pet.specie == query_pet.specie
    assert new_pet.age == query_pet.age
    assert new_pet.user_id == query_pet.user_id

    engine.execute("DELETE FROM pets WHERE id={}".format(new_pet.id))


def test_select_pet():
    """ Should select a pet in Pets table and compare it """

    pet_id = faker.random_number(digits=4)
    name = faker.name()
    specie = "dog"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    specie_mock = AnimalTypes("dog")

    data_mock = Pets(id=pet_id, name=name, specie=specie_mock, age=age, user_id=user_id)

    engine = db_connect.get_engine()
    engine.execute(
        "INSERT INTO pets (id, name, specie, age, user_id) VALUES ('{}','{}','{}','{}','{}');".format(
            pet_id,
            name,
            specie,
            age,
            user_id,
        )
    )

    query_select1 = pet_repository.select_pet(pet_id=pet_id)
    query_select2 = pet_repository.select_pet(user_id=user_id)
    query_select3 = pet_repository.select_pet(pet_id=pet_id, user_id=user_id)

    assert data_mock.id == query_select1[0].id
    assert data_mock.id == query_select2[0].id
    assert data_mock.id == query_select3[0].id

    engine.execute("DELETE FROM pets WHERE id={}".format(pet_id))

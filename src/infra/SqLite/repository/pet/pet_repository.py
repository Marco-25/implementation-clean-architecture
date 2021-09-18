from src.domain.models import Pets
from src.infra.SqLite.config import DBConnectionHandler
from src.infra.SqLite.entities import Pets as PetModel


class PetRepository:

    @classmethod
    def insert_pet(cls, name: str, specie: str, age: int, user_id: int) -> Pets:

        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetModel(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()
                return Pets(
                    new_pet.id,
                    new_pet.name,
                    new_pet.specie.value,
                    new_pet.age,
                    new_pet.user_id
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

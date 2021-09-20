from typing import List, Union, Optional
from src.data.interfaces import PetRepositoryInterface
from src.domain.models import Pets
from src.infra.SqLite.config import DBConnectionHandler
from src.infra.SqLite.entities import Pets as PetsModel


class PetRepository(PetRepositoryInterface):

    @classmethod
    def insert_pet(cls, name: str, specie: str, age: Optional[int], user_id: int) -> Pets:

        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetsModel(name=name, specie=specie, age=age, user_id=user_id)
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

    @classmethod
    def select_pet(cls, user_id: int = None, pet_id: int = None) -> Union[List[Pets], None]:

        try:
            query = None

            if pet_id and not user_id:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(PetsModel).filter_by(id=pet_id).one()
                    query = [data]

            if not pet_id and user_id:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(PetsModel).filter_by(user_id=user_id).all()
                    query = data

            if user_id and pet_id:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(PetsModel).filter_by(id=pet_id, user_id=user_id).one()
                    query = [data]

            return query

        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

        return None

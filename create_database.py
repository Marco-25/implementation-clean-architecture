from src.infra.SqLite.config import *
from src.infra.SqLite.entities import *


def create_database():
    db_connect = DBConnectionHandler()
    engine = db_connect.get_engine()
    Base.metadata.create_all(engine)


create_database()

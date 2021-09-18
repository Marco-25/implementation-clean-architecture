from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """ Sqlalchemy database connection"""

    def __init__(self) -> None:
        self.__connection_string: str = "sqlite:///database.db"
        self.session: None = None

    def get_engine(self):
        """ 
            Return connection Engine
            :param - None
            :return - engine connection to Database
        """
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_marker = sessionmaker()
        self.session = session_marker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

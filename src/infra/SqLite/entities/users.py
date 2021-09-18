from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.infra.SqLite.config import Base


class Users(Base):
    """Users Entity"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    id_pet = relationship("Pets")

    def __rep__(self) -> str:
        return f"User [name={self.name}]"

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "password": self.password
        }

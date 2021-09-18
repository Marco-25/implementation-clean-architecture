import enum
from sqlalchemy import Column, String, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.SqLite.config import Base


class AnimalTypes(enum.Enum):
    """ Defining Anymals Types """
    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"


class Pets(Base):
    """ Pets Entity """

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))

    def __rep__(self) -> str:
        return f"User \
                [name={self.name},\
                specie={self.specie}, \
                user_id={self.user_id}]"

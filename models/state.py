#!/usr/bin/python3
"""
State Module for HBNB project
"""

from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    State class
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """
            Getter attribute
            """

            from models import storage
            my_city = []
            for list_cities in storage.all(City).values():
                if list_cities.state_id == self.id:
                    my_city.append(list_cities)
            return my_city

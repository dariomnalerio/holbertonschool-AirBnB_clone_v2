#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):

    name = Column(String(128), nullable=False)
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            from models.city import City
            from models import storage
            cities_list = []
            for item in storage.all(City):
                if storage.all(City)[item].state_id == self.id:
                    cities_list.append(storage.all(City)[item])
            return cities_list
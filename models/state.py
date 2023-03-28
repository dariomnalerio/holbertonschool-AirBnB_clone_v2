#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):
        from models.city import City
        return [obj for obj in models.storage.all(City).values() if
                obj.state_id == self.id]

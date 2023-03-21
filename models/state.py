#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')

    else:
        @property
        def cities(self):
            """
            returns a list of City instances with
            state_id matching the current State.id
            """
            from models import storage
            cities = storage.all("City")
            return [city for city in cities.values() if city.state_id == self.id]

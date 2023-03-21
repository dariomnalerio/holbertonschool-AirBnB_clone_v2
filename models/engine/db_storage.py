#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
USER = os.environ.get('HBNB_MYSQL_USER')
PSWD = os.environ.get('HBNB_MYSQL_PWD')
HOST = os.environ.get('HBNB_MYSQL_HOST')
DB = os.environ.get('HBNB_MYSQL_DB')
ENV = os.environ.get('HBNB_ENV')

class DBStorage():
    """Class method"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            USER, PSWD, HOST, DB), pool_pre_ping=True)
        if ENV == 'test':
            Base.metadata.drop_all(self.__engine)
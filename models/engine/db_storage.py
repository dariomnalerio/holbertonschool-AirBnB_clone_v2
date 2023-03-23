#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



class DBStorage():
    """Class method"""
    __engine = None
    __session = None

    classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
    }

    def __init__(self):

        self.__engine = create_engine(('{}+{}://{}:{}@{}/{}')
                                      .format("mysql", "mysqldb",
                                              getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        objs = {}
        for class_item in self.classes:
            if self.classes[class_item] == cls or cls is None:
                for key in self.__session.query(self.classes[class_item]).all():
                    objs[f"{key.__class__.__name__}.{key.id}"] = key
        return objs

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

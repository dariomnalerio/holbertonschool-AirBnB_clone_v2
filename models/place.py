#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table(
    "place_amenity", Base.metadata,
    Column("place_id", String(60),
           ForeignKey("places.id"), nullable=False),
    Column("amenity_id", String(60),
           ForeignKey("amenities.id"), nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []


    reviews = relationship("Review", cascade="all, delete-orphan",
                        backref='place')
    amenities = relationship("Amenity", secondary=place_amenity,
                            backref="places", viewonly=False)

    @property
    def reviews(self):
        """ Return all reviews for a place """
        return [Review.all(Review.place_id == self.id)]

    @property
    def amenities(self):
        """ Return all amenities for a place """
        return [Amenity.all(Amenity.id == self.id)]

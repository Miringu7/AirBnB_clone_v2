#!/usr/bin/python3
"""This is the place class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
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
    #amenity_ids = []

    if getenv['HBNB_TYPE_STORAGE'] == 'db':
        reviews = relationship("Review", cascade="all, delete, delete-orphan", backref="place")
    else:
        @property
        def reviews(self):
            """returns the cities in this State """
            from models import storage
            review_instances = []
            for value in storage.all(Place).values():
                if value.place_id == self.id:
                    review_instances.append(value)
            return review_instances


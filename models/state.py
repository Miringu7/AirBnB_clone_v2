#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import os
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


storage_type = os.getenv("STORAGE_TYPE")
class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # For DBStorage
    if storage_type == 'db':
        cities = relationship("City", backref="state", cascade="all, delete-orphan")

    # For FileStorage
    if storage_type == 'file':
        @property
        def cities(self):
            """ Getter attribute for cities """
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
                return city_list

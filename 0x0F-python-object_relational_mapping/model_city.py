#!/usr/bin/python3
""" Contains the class definition of a city """

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ Class that defines each city """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

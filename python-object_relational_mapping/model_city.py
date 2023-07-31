#!/usr/bin/python3
"""
Module that contains the class definition of a City.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    City class inherits from Base and links to the MySQL table 'cities'.

    Attributes:
        id (int): Represents a column of an auto-generated, unique integer,
                  can't be null and is a primary key.
        name (str): Represents a column of a string of 128 characters,
                    can't be null.
        state_id (int): Represents a column of an integer, can't be null,
                        and is a foreign key to states.id.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

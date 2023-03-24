#!/usr/bin/python3
""" city model """

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class City(Base, State):
    """
    Class with id amd name attribute of city linked to state with foriegn key
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey(State.id))

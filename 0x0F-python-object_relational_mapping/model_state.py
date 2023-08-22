#!/usr/bin/python3
"""Defines the class State and Base, an instance
of declarative_base() """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

theMetadata = MetaData()
Base = declarative_base(metadata=theMetadata)


class State(Base):
    """
    class with an id and name attribute of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

#!/usr/bin/python3
"""ORM demonstration"""


import sys
from sqlalchemy import create_engine, Column
from sqlalchemy import String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """State class"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name

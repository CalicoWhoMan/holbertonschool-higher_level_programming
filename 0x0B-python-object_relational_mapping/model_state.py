#!/usr/bin/python3
"""A PY file that contains the class def of 'State'"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class that inherits from 'Base', links to SQL table 'states"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(String(128), nullable = False)

#!/usr/bin/python3
"""PY file that contains the class def of a 'City'"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):i
    """class for City"""
    __tablename__ = 'cities'

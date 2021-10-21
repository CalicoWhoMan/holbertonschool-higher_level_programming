#!/usr/bin/python3
"""
Class Base
"""


import json


class Base:
    """
    Class for file Base
    """
    __nb_objects = 0


    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

    @classmethod
    def save_to_file(cls, list_objs):

    @staticmethod
    def from_json_string(json_string):

    @classmethod
    def create(cls, **dictionary):

    @classmethod
    def load_from_file(cls):

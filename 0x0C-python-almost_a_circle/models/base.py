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
        """
        initializing base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string rep of list_dictionaries
        """
        listdict2 = []
        if list_dictionaries is None or list_dictionaries == "":
            return ("[]")
        else:
            listdict2 = json.dumps(list_dictionaries)
        return listdict2

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the json string rep of list_objs to file
        """
        with open(cls.__name__ + ".json", 'w') as savetofile:
            if list_objs is None:
                savetofile.write('[]')
            else:
                savetofile.write(cls.to_json_string([item.to_dictionary()
                for item in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the json string rep
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

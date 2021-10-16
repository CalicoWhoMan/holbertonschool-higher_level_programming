#!/usr/bin/python3
"""
Fnction that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


import json


def class_to_json(obj):
    """
    returns dict desc for json cerealization of obj
    """
    return vars(obj)

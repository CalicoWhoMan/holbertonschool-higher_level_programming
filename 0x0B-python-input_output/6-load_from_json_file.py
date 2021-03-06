#!/usr/bin/python3
"""
Function that creates an Object from a "JSON file"
"""


import json


def load_from_json_file(filename):
    """
    created object from json file
    """
    with open(filename) as f:
        return json.loads(f.read())

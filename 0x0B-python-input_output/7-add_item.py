#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then save them to a file
"""


import sys
import json


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


try:
    creates_f = load_from_json_file("add_item.json")
except:
    creates_f = []


creates_f += sys.argv[1:]


save_to_json_file(creates_f, "add_item.json")

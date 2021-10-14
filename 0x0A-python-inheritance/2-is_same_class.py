#!/usr/bin/python3
"""
F that returns True if object is exactly an instance of 
the specified class, otherwise is False
"""


def is_same_class(obj, a_class):
    """
    True if identical otherwise Fals
    """
    return type(obj) == a_class

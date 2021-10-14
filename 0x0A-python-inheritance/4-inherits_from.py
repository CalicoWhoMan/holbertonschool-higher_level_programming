#!/usr/bin/python3
"""
F that returns True if object is an instance of a class that inherited
(directly or indirectle) from the specified class otherwise False
"""


def inherits_from(obj, a_class):
    """
    returns True of False DOC
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)

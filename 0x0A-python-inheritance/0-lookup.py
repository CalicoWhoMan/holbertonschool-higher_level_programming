#!/usr/bin/python3
"""
Function that returns the list of available
attributes and methods of an object using
def lookup(obj):
returns a list
"""


def lookup(obj):
    """
    Returns a list
    """
    return dir(obj)

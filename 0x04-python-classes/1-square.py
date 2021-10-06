#!/usr/bin/python3
""" Square class defined by size """


class Square:
    """ Size for square parameters """
    def __init__(self, size=0):
        self.size__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
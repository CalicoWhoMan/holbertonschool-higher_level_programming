#!/usr/bin/python3
"""Square class"""


class Square:
    """ Square class size parameters """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    """ class Square area size """

    def area(self, size=0):
        square_area_size = self.__size ** 2
        return square_area_size

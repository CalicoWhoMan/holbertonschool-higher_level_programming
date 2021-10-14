#!/usr/bin/python3
"""
Class Square inheriting 09 with Area and Size
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square Class with Size and Area
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

        def area(self):
            return self.__size * self.__size

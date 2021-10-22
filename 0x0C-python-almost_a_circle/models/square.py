#!/usr/bin/python3
"""
class Square inheriting class Rectangle/base
"""


from models.rectangle import Rectangle


class Square(Rectangle):
"""
setting up class Square
"""

    def __init__(self, size, x=0, y=0, id=None):
    """
    init for Square
    """
        super().__init__(size, size, x, y, id)

    def __str__(self):
    """
    replacing the str method
    """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    @property
    """
    getter for size
    """
    def size(self):
        return self.width

    @size.setter
    """
    setter for size
    """
    def size(self, value):
        self.width = value
        self.height = value

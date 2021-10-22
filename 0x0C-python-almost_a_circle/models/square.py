#!/usr/bin/python3
"""
class Square inheriting class Rectangle/base
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    setting up class for square
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
    def size(self):
        """
        getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for size
        """
        self.width = value
        self.height = value

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

    def update(self, *args, **kwargs):
        """
        assigns attributes to Square class
        """
        list2 = ["id", "size", "x", "y"]
        if args and args[0] is not None:
            for rang2 in range(len(args)):
                setattr(self, list2[rang2], args[rang2])
        else:
            for key, value in kwargs.items():
                self.__setattr__( key, value)

    def to_dictionary(self):
        """
        returns dict repr of a Square
        """
        the_dict2 = {}

        the_dict2['id'] = self.id
        the_dict2['size'] = self.size
        the_dict2['x'] = self.x
        the_dict2['y'] = self.y
        return the_dict2

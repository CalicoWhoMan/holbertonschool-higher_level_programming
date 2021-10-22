#!/usr/bin/python3
"""
Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class inherited from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    """
    getter for width
    """
    def width(self):
        return self.__width

    @width.setter
    """
    setter for width
    """
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    """
    getter for height
    """
    def height(self):
        return self.__height

    @height.setter
    """
    setter for height
    """
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    """
    getter for x
    """
    def x(self):
        return self.__x

    @x.setter
    """
    setter for x
    """
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    """
    getter for y
    """
    def y(self):
        return self.__y

    @y.setter
    """
    setter for y
    """
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
    """
    Area for the rectangle
    """
        return self.__width * self.__height

    def display(self):
    """
    prints # characters
    """
        for horiz in range(self.__y):
            print("")
        for horiz in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
    """
    overrides the str method
    """
        return("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
    """
    assigns arg to each attr
    """
        a_list = ["id", "width", "height", "x", "y"]
        if args and args[0] is not None:
            for rang in range(len(args)):
                setattr(self, a_list[rang], args[rang])

    def to_dictionary(self):
    """
    returns dictionarry rep
    """
        the_dict = {}

        the_dict['id'] = self.id
        the_dict['width'] = self.width
        the_dict['height'] = self.height
        the_dict['x'] = self.__x
        the_dict['y'] = self.__y
        return the_dict

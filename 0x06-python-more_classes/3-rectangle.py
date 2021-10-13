#!/usr/bin/python3
#!/usr/bin/python3
"""
This program writes a class called Rectangle
that defines a rectangle by width and height
based on task 0
Contains new area & perimeter of rectanglei
Contains new string with char # to make shape
Contains NEW repr function that returns
a printable representation of the given
object
"""


class Rectangle:
    """
    Rectangle
    """
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        area = self.__width * self.__height
        return area

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        perimeter = (2 * self.__width) + (2 * self.__height)
        return perimeter

    def __str__(self):
        """
        += allows the string to not set itself but to add on instead
        """
        hashstr = ""
        if self.__width == 0 or self.__height == 0:
            return hashstr
        for H in range(self.height):
            for W in range(self.width):
                hashstr += "#"
            hashstr += "\n"
        return hashstr[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

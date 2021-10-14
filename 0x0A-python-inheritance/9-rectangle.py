#!/usr/bin/python3
"""
Class called Rectangle that inherits number 7 
adding Width and Height
NEW 09
Adding Area and String that returns the following rectangle description
[Rectangle] <width>/<height>
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class with Height and Weight
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    
    def area(self):
        area = self.__width * self.__height
        return area

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

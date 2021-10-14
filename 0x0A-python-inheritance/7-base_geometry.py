#!/usr/bin/python3
"""
Replicate 06 and adds F integer_validator with TypeError and ValueError
"""


class BaseGeometry:
    """
    Empty empty class class
    """

    def area(self):
        """
        Documentation for Exception"
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates Value, Name is a string
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

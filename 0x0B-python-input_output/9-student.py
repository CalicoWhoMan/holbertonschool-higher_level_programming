#!/usr/bin/python3
"""
Write a class Student that defines a student by >
"""


class Student:
    """
    class student student
    """

    def __init__(self, first_name, last_name, age):
        """
        class specifications for student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves dictonary reps of student class
        """
        return vars(self)

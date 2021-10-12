#!/usr/bin/python3
"""
Function that prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for x in text:
        if x == '.' or x == '?' or x == ':':
            print("{}\n".format(x))
        else:
            print(x, end="")

#!/usr/bin/python3
"""
Fnction that writes a string to a text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    string to file
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)

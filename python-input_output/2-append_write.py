#!/usr/bin/python3
"""
Module that defines a function to append a string to a UTF-8 text file
and return the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF-8 encoded text file and
    returns the number of characters added.

    The file is created if it does not exist.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to add at the end of the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

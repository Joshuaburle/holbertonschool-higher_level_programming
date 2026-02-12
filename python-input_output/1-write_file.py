#!/usr/bin/python3
"""
Module that defines a function to write a string to a UTF-8 text file
and return the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 encoded text file and returns
    the number of characters written.

    The file is created if it does not exist.
    The content is overwritten if the file already exists.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write into the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

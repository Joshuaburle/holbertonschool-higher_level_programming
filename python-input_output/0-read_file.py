#!/usr/bin/python3
"""
Module that defines a function to read a UTF-8 text file
and print its content to standard output.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

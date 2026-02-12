#!/usr/bin/python3
"""
Module that defines a function to return the dictionary
description of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.

    All attributes of the object are assumed to be serializable
    (list, dictionary, string, integer, and boolean).

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__

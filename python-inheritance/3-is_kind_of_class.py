#!/usr/bin/python3
"""Module that defines a function to check instance or inherited class."""

def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of or inherited from a_class."""
    return isinstance(obj, a_class)

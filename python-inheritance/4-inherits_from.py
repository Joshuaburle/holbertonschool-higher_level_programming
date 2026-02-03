#!/usr/bin/python3
"""Module that defines a function to check inherited class only."""

def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a subclass of a_class."""
    return isinstance(obj, a_class) and type(obj) != a_class

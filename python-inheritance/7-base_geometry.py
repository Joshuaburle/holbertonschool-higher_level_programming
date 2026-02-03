#!/usr/bin/python3
"""Module that defines a BaseGeometry class with validation methods."""

class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raises an Exception indicating that area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

#!/usr/bin/python3
"""Module that defines a full Rectangle class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with area calculation and string representation."""

    def __init__(self, width, height):
        """Initializes a Rectangle with validated private width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

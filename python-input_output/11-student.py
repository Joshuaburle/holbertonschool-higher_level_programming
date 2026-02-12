#!/usr/bin/python3
"""
Module that defines a Student class with JSON serialization
and deserialization helpers.
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes whose names are in
        attrs are returned. Otherwise, all attributes are returned.

        Args:
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: The dictionary representation of the student.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.

        Args:
            json (dict): Dictionary where keys are attribute names and values
                         are the new values for those attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)

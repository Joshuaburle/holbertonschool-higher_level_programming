#!/usr/bin/env python3
"""
Pickling Custom Classes
Serialize and deserialize a custom Python object using pickle.
"""

import pickle


class CustomObject:
    """Custom class that can be serialized using pickle."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.

        Args:
            filename (str): The file where the object will be stored
        Returns:
            None if error occurs
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (pickle.PickleError, OSError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        Args:
            filename (str): The file to load the object from
        Returns:
            CustomObject instance or None if error occurs
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)

                # Ensure the loaded object is actually a CustomObject
                if isinstance(obj, cls):
                    return obj
                return None

        except (FileNotFoundError, pickle.PickleError, EOFError, OSError):
            return None

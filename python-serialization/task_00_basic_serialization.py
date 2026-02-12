#!/usr/bin/env python3
"""
Basic Serialization Module
Provides functions to serialize a dictionary to a JSON file
and deserialize it back into a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): The dictionary to serialize
        filename (str): The JSON file to write to
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it into a Python dictionary.

    Args:
        filename (str): The JSON file to read from

    Returns:
        dict: The deserialized Python dictionary
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

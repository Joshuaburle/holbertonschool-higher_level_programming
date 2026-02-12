#!/usr/bin/env python3
"""
XML Serialization and Deserialization
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): dictionary to serialize
        filename (str): output XML file
    """
    # Create root element
    root = ET.Element("data")

    # Add dictionary items as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create tree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """
    Deserialize XML file back into a Python dictionary.

    Args:
        filename (str): XML file to read

    Returns:
        dict: reconstructed dictionary
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result

    except (ET.ParseError, FileNotFoundError, OSError):
        return None

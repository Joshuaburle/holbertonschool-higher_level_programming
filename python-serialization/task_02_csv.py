#!/usr/bin/env python3
"""
Convert CSV data into JSON format
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert CSV file content into JSON and save it into data.json

    Args:
        filename (str): CSV input file

    Returns:
        True if conversion successful, False otherwise
    """
    try:
        data = []

        # Read CSV file
        with open(filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                data.append(row)

        # Write JSON file
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except (FileNotFoundError, PermissionError, csv.Error, OSError):
        return False

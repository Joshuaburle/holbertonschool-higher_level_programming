#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Return the sum of unique integers in a list."""
    unique_numbers = set(my_list)
    return sum(unique_numbers)

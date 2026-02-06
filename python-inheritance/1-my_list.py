#!/usr/bin/python3
"""Defines MyList class extending list with a sorted display method."""


class MyList(list):
    """List extension that can print its items sorted."""

    def print_sorted(self):
        """Prints the list in ascending order without changing it."""
        print(sorted(self))

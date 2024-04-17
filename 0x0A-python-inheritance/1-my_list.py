#!/usr/bin/python3

"""Defines MyList class"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in ascending sorted."""
        print(sorted(self))

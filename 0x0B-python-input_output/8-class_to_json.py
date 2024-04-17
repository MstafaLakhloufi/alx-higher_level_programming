#!/usr/bin/python3
"""Module containing the function class_to_json"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__

#!/usr/bin/python3
"""Module containing the function to_json_string."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)

#!/usr/bin/python3
"""Defines an object attribute lookup function."""



def lookup(obj):
    """Looks up object attributes and methods.
    Args:
        obj (object): the object to list.

    Returns:
        list: the list of attributes.
    """
    return dir(obj)

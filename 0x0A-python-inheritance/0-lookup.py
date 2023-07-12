#!/usr/bin/python3
''' This module defines the function lookup(obj) '''


def lookup(obj):
    ''' returns the list of available attributes and methods of an object
    Args:
        obj (any): the object to look up

    '''

    return (dir(obj))

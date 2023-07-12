#!/ussr/bin/python3
''' This module defines the function lookup(obj) '''


def lookup(obj):
    ''' returns the list of available attributes and methods of an object
    Args:
        obj (object): the object to look up

    Returns:
        A list
    '''

    return (dir(obj))

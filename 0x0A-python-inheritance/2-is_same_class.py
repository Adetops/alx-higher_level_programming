#!/usr/bin/python3
''' Module that defines this function is_same_class(obj, a_class) '''


def is_same_class(obj, a_class):
    ''' function that checks the instance of a specified object
    Args:
        obj (object): any data structure
        a_class (class): data type to consider

    Returns:
        True if obj is exactly an instance of a_class
        False otherwise
    '''

    return (True if isinstance(obj, a_class) else False)

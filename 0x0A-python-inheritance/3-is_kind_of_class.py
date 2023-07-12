#!/usr/bin/python3
''' Module that defines the function is_kind_of_class(obj, a_class) '''


def is_kind_of_class(obj, a_class):
    ''' Checks the instance of an object with a class and subclass
    Args:
        obj (any): the object to check
        a_class (class): the class to check from

    Returns:
        Either True or False
    '''
    return (True if isinstance(obj, a_class) else False)

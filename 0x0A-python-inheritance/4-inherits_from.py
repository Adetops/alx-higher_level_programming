#!/usr/bin/python3
''' Module that defines the function inherits_from(obj, a_class) '''


def inherits_from(obj, a_class):
    ''' Checks instance of an object with subclass only
    Args:
        obj (any): any object which instance to check
        a_class (str): the class to check its subclass

    Returns:
        Either True or False
    '''

    if (isinstance(obj, a_class) and (type(obj) != a_class)):
        return True
    else:
        return False

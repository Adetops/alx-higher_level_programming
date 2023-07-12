#!/usr/bin/python3
''' Module that defines to_json_string(my_obj) function '''


import json


def to_json_string(my_obj):
    ''' function that returns the JSON representation of an object (string):
    Args:
        my_obj (obj): any object representation

    Returns:
        JSON representation of an object (string)
    '''

    return (json.dumps(my_obj))

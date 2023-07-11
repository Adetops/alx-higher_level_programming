#!/usr/bin/python3
''' Module that defined the function from_json_string(my_str) '''


import json

def from_json_string(my_str):
    ''' function that returns an object represented by a JSON string
    Args:
        my_str (str): the string to deserialize

    Returns:
        An object rep
    '''
    return (json.loads(my_str))

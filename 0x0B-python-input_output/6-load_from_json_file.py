#!/usr/bin/python3
''' Module that defines load_from_json_file(filename) functiom '''


import json


def load_from_json_file(filename):
    ''' Funtiom that creates an Object from JSON file
    Args:
        filename (str): name of the file
    '''

    with open(filename, mode='r') as f:
        my_obj = json.load(f)
        return my_obj

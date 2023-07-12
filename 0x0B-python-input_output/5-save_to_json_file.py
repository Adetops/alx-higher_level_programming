#!/usr/bin/python3
''' Module that defines save_to_json_file(my_obj, filename) function '''


import json

def save_to_json_file(my_obj, filename):
    ''' function that writes an Object to a text file
    Args:
        my_obj (obj): any data structure
        filename (str): name of the file to write to
    '''

    with open(filename, mode='w', encoding='UTF8') as f:
        json.dump(my_obj, f)

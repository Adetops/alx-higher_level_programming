#!/usr/bin/python3
""" This module defined the function write_file(filename="", text="") """


def write_file(filename="", text=""):
    ''' Writes a str to a txt file and return the number of chars written
    Args:
        filename (str): name of the file
        text (str): the string text to write to the file
    '''

    with open(filename, mode='w', encoding='UTF8') as f:
        return (f.write(text))

#!/usr/bin/python3
''' This module defines the function append_write(filename="", text="") '''


def append_write(filename="", text=""):
    ''' function that appends a string at the end of a text file
    Args:
        filename (str): name of the file
        text (str): string text to append

    Return:
        number os characters added.
    '''

    with open(filename, mode='a', encoding='UTF8') as f:
        return (f.write(text))

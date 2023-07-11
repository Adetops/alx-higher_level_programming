#!/usr/bin/python3
""" This module defines the function read_file(filename="") """


def read_file(filename=""):
    """ Function that reads a text file and prints it to stdout
    Arg:
        filename (str): name of the file to read from
    """

    with open(filename, encoding='UTF8') as f:
        for line in f:
            print(line, end='')

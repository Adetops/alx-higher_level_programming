#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    length = len(argv) - 1
    suffix = 'arguments:'
    if length == 1:
        suffix = 'argument:'
    elif length == 0:
        suffix = 'arguments.'
    print(length, suffix)
    for each in range(1, length + 1):
        print('{:d}:'.format(each), argv[each])

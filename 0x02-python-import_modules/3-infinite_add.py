#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    res = 0
    for value in range(1, len(argv)):
        args = int(argv[value])
        res += args
    print(res)

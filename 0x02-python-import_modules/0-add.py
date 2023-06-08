#!/usr/bin/python3
if __name__ == '__main__':
    from add_0 import add
    '''My addition function

    Args:
        a: first integer
        b: second integer

    Return:
        Added values and the result. a + b = sum
    '''
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

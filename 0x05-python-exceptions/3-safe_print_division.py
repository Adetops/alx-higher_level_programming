#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = "{}".format(a / b)
    except (ZeroDivisionError, TypeError, ValueError):
        div = "{}".format("None")
    finally:
        print("Inside result: {}".format(div))
    return (div)

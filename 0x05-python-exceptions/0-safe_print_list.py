#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real_num = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            real_num += 1
    except IndexError:
        pass
    print()
    return (real_num)

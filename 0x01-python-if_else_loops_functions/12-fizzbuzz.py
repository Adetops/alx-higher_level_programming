#!/usr/bin/python3
def fizzbuzz():
    for h in range(1, 101):
        if h % 3 == 0 and h % 5 == 0:
            print('FizzBuzz', end=' ')
        elif h % 3 == 0 and h % 5 != 0:
            print('Fizz', end=' ')
        elif h % 5 == 0 and h % 3 != 0:
            print('Buzz', end=' ')
        else:
            if (h == 100):
                print(h)
            print(h, end=' ')

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = int(str(number)[-1])
if number < 0:
    l_digit = -l_digit
if l_digit > 5:
    l_str = "greater than 5"
elif l_digit == 0:
    l_str = "0"
else:
    l_str = "less than 6 and not 0"
print("Last digit of {} is {} and is {}".format(number, l_digit, l_str))

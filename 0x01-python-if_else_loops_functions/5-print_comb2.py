#!/usr/bin/python3
for h in range(0, 100):
    if h == 99:
        print(h)
    else:
        print("{:02d}".format(h), end=", ")

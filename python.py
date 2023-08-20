#!/usr/bin/python3

class MyClass:
    def __init__(self, my_attribute):
        self.my_attribute = my_attribute

    def my_method(self):
        print("HEllo, World!")

class subClass(MyClass):
    def testy(self):
        print("This is a test")


my_test = subClass('2')
print(my_test.my_attribute)
print(my_test.my_method())
print(my_test.testy())
print(subClass.__bases__)

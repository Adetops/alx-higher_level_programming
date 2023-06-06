#!/usr/bin/python3

class Adeleke:
    def __init__(self, family, name, position, age):
        self.family = family
        self.name = name
        self.position = position
        self.age = age


A = Adeleke('John Taiwo', 'Heritage', 'Second', 22)
B = Adeleke('Adekunle', 'Mayowa', 'Second', 23)
C = Adeleke('Ogoigbe', 'Glory', 'First', 28)
for elem in A, B, C:
    print(elem.family, '\t', elem.name, '\t', elem.position, '\t', elem.age)

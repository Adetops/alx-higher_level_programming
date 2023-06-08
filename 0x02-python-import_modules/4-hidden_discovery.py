#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    names = []
    for name in dir(hidden_4):
        if (name[0] != '_' and name[1] != '_'):
            print(name)
#            names.append(name)
#    for i in range(0, len(names)):
#       print(names[i])

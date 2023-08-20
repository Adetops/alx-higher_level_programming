def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in iter(kwargs):
            print("{} == {}".format(key, value))


key = dict(name="yahoo")
greet_me(**key)

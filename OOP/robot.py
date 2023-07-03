class Robot:
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year
    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a Robot without a name")
    def set_name(self, name):
        self.__name = name
    def get_name(self, name):
        return self.__name
    def set_buildYear(self, by):
        self.__build_year = by
    def get_buildYear(self, by):
        return self.__build_year
    def __repr__(self):
        return "Robot('" + self.__name + "', " + str(self.__build_year) + ")"
    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " + str(self.__build_year)
if __name__ == "__main__":
    x = Robot("Marvin", 1950)
    x.say_hi()
    y = Robot("Herit")
    y.say_hi()
    z = Robot("Josh", 2006)
    z.say_hi()

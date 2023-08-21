from abc import ABC, abstractmethod
# property helps you to avoid replacing with setter and getter functions 

class Polygon(ABC):
    name = "Polygon"
    @abstractmethod
    def side(self):
        pass

class Square(Polygon):
    name = "Square"
    def __init__(self,side):
        self.__side = side


    @property
    def side(self):
        return self.__side
    
    @side.setter
    def side(self,side):
        self.__side = side

    @staticmethod
    def describe():
        return ("I am a square")
    
    @classmethod
    def describe_my_class(cls):
        return (f"I am of the type {cls.name}")

    def describe_me(self):
        return f"I am a {self.__class__.name} with side {self.__side}"

if __name__ == "__main__":
    s1 = Square(5)
    print (s1.describe())
    print (s1.describe_my_class())
    print (s1.describe_me())
    # this is where property decorator helps. __side is not acceesible directly. Property helps you to wrap the same.
    s1.side = 7
    print (s1.describe_me())
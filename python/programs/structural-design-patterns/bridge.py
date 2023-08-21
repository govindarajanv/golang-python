from abc import ABC,abstractmethod

#Decouple an abstraction from its implementation so that the two can vary independently.
#we separate an abstraction and its implementation and develop separate inheritance structures for both the abstraction and the implementer.

class Color(ABC):
    @abstractmethod
    def fill(self):
        pass

class Red(Color):
    def fill(self):
        return "Red"

class Blue(Color):
    def fill(self):
        return "Blue"

class Shape(ABC):
    @abstractmethod
    def display(self):
        pass

class Circle(Shape):
    def __init__(self,color):
        self.color = color
    def display(self):
        print (f"Displaying a {self.color.fill()} {self.__class__.__name__}")

class Rectangle(Shape):

    def __init__(self,color):
        self.color = color

    def display(self):
        print (f"Displaying a {self.color.fill()} {self.__class__.__name__}")

if __name__ == "__main__":

    shape1 = Rectangle(Red())
    shape1.display()
    shape2 = Rectangle(Blue())
    shape2.display()
    shape3 = Circle(Red())
    shape3.display()
    shape4 = Circle(Blue())
    shape4.display()
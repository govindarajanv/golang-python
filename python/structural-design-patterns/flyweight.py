from enum import Enum
from abc import abstractmethod, ABC

class Pen(ABC):
    @abstractmethod
    def setColor(self, color):
        pass

    @abstractmethod
    def draw(self, content):
        pass


class BrushSize(Enum):
    THIN = 1
    MEDIUM = 2
    THICK = 3


class ThickPen(Pen):
    brushSize = BrushSize.THICK
    color = None

    def setColor(self, color):
        self.color = color

    def draw(self, content):
        print(f"Drawing content: {content} in color: {self.color} with brush size: {self.brushSize}")


class ThinPen(Pen):
    brushSize = BrushSize.THIN
    color = None

    def setColor(self, color):
        self.color = color

    def draw(self, content):
        print(f"Drawing content: {content} in color: {self.color} with brush size: {self.brushSize}")


class MediumPen(Pen):
    brushSize = BrushSize.MEDIUM
    color = None

    def setColor(self, color):
        self.color = color

    def draw(self, content):
        print(f"Drawing content: {content} in color: {self.color} with brush size: {self.brushSize}")
        
class PenFactory:
    pens = {}

    @staticmethod
    def getThickPen(color):
        key = color + "-THICK"
        if key not in PenFactory.pens:
            pen = ThickPen()
            pen.setColor(color)
            PenFactory.pens[key] = pen
        return PenFactory.pens[key]

    @staticmethod
    def getThinPen(color):
        key = color + "-THIN"
        if key not in PenFactory.pens:
            pen = ThickPen()
            pen.setColor(color)
            PenFactory.pens[key] = pen
        return PenFactory.pens[key]


    @staticmethod
    def getMediumPen(color):
        key = color + "-MEDIUM"
        if key not in PenFactory.pens:
            pen = ThickPen()
            pen.setColor(color)
            PenFactory.pens[key] = pen
        return PenFactory.pens[key]

if __name__ == "__main__":
        pen1 = PenFactory.getThickPen("YELLOW")
        pen1.draw("flyweight")
        pen2 = PenFactory.getThickPen("YELLOW")
        pen2.draw("flyweight")
        pen3 = PenFactory.getThinPen("YELLOW")
        pen3.draw("flyweight")
        pen4 = PenFactory.getThickPen("BLUE")
        pen4.draw("flyweight")
        print(pen1 == pen2,pen1.__hash__(),pen2.__hash__())
        print(pen3.__hash__())
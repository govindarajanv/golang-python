from abc import ABC,abstractmethod
from enum import Enum,auto

class HotDrinks(ABC):
    @abstractmethod
    def consume(self):
        pass
    
class Coffee(HotDrinks):
    
    def consume(self):
        print ("Coffee is being consumed")
        
class Tea(HotDrinks):
    
    def consume(self):
        print ("Tea is being consumed")
        
class HotDrinksFactory(ABC):
    
    @abstractmethod
    def prepare(self,quantity):
        pass
    
class CoffeeFactory(HotDrinksFactory):
    
    def prepare(self,quantity):
        return Coffee()
        
class TeaFactory(HotDrinksFactory):
    
    def prepare(self,quantity):
        return Tea()
        
class HotDrinksMachine:
    class AvailableDrinks(Enum):
        COFFEE = auto()
        TEA = auto()
        
    __factories = {}
    __initialized = False
    def __init__(self):

        
        if not self.__initialized:
            self.__initialized = True
            for drink in self.AvailableDrinks:
                factory = drink.name[0] + drink.name[1:].lower() + "Factory"
                self.__factories[drink.name] = factory
        print (self.__factories)
    def prepare(self):
        choice = input("Enter your choice [Coffee/Tea]")
        print (choice.upper())
        available_drinks = [member.name for member in self.AvailableDrinks]
        print (values)
        if choice.upper() in available_drinks:
            print (self.__factories[choice.upper()])
            factory = eval(self.__factories[choice.upper()])()
            return factory.prepare(200)
        else:
            raise ValueError ("Not a valid option")
            
                    
if __name__ == "__main__":
    hd = HotDrinksMachine()
    
    beverage = hd.prepare()
    beverage.consume()
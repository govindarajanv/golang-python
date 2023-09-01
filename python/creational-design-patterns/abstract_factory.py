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
        
    __initialized = False
    __factories = {}
    
    def __init__(self):
        if not self.__initialized:
            self.__initialized = True
            for drink in self.AvailableDrinks:
                factory = drink.name[0] + drink.name[1:].lower() + "Factory"
                self.__factories[drink.name] = factory
        print (self.__factories)
                
    def prepare(self):
        
        choice = input("Please choose your beverage. [Coffee/Tea]:")
        available_drinks = [member.name for member in self.AvailableDrinks]
        if choice.upper() in available_drinks:
            factory = eval(self.__factories[choice.upper()])()
            return factory.prepare(200)
        else:
            raise ValueError("Invalid Option")
            
if __name__ == "__main__":
    hd = HotDrinksMachine()
    beverage = hd.prepare()
    beverage.consume()
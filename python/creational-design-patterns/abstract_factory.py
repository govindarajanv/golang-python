from abc import ABC,abstractmethod
from enum import Enum,auto

class HotDrinks:
    
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
    def prepare(self):
        pass
    
class CoffeeFactory(HotDrinksFactory):
    
    def prepare(self):
        return Coffee()
        
class TeaFactory(HotDrinksFactory):
    
    def prepare(self):
        return Tea()        

class HotDrinksMachine:
    class AvailableDrinks(Enum):
        COFFEE = auto()
        TEA = auto()
    
    __initialized = False
    __factories = {}
    
    # get a dictionary of <beverage_name> : <its factory>
    def __init__(self):
        if not self.__initialized:
            self.__initialized = True
            for drink in self.AvailableDrinks:
                factory = drink.name[0].upper()+drink.name[1:].lower() + "Factory"
                self.__factories[drink.name] = factory
            print (self.__factories)
    
    # get the choice, parse the available drinks to arrive at factories, call factory to get beverage 
    def dispense(self):
        choice = input("Please choose your beverage. [Coffee/Tea]:")
        
        # assert choice.lower() == "coffee" or choice.lower() == "tea", "Invalid Option
        
        available_drinks = self.AvailableDrinks._member_names_
        # available_drinks = [ member.name for member in self.AvailableDrinks ] # this is also an option
        if choice.upper() in available_drinks:
            factory_name = self.__factories[choice.upper()]
            factory_obj = eval(factory_name)()
            beverage = factory_obj.prepare()
            return beverage
        else:
            raise AssertionError("Invalid Option")
    
    
if __name__ == "__main__":
    hm = HotDrinksMachine()
    beverage = hm.dispense()
    beverage.consume()
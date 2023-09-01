from abc import ABC 
from enum import Enum,auto

class HotDrinks(ABC):
    def consume(self):
        pass

class Coffee(HotDrinks):
    def consume(self):
        print ("Coffee was very aromatic!!!")

class Tea(HotDrinks):
    def consume(self):
        print ("I had a flavourful Tea!!!")

class HotDrinksFactory(ABC):
    def prepare(self,quantity):
        pass

class CoffeeFactory(HotDrinksFactory):
    def prepare(self,quantity):
        print (f"Coffee is being prepared. You will be served {quantity} ml of Coffee")
        return Coffee()

class TeaFactory(HotDrinksFactory):
    def prepare(self,quantity):
        print (f"Tea is being prepared. You will be served {quantity} ml of Tea")
        return Tea()

class HotDrinkMachine:
    class AvailableDrink(Enum):  # violates OCP
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))


    def make_drink(self):
        print('Available drinks:')
        for f in self.factories:
            print(f[0])


        s = input(f'Please pick drink (0-{len(self.factories)-1}): ')
        try:
            idx = int(s)
            if idx < 0 or idx >= 2:
                raise ValueError("Only 0 or 1 is expected") 
        except Exception as err:
            raise RuntimeError(err)
        else:    
            return self.factories[idx][1].prepare(150)


if __name__ == '__main__':

    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()
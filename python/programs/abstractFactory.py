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
        idx = int(s)
        s = input(f'Specify quantity: ')
        quantity = int(s)
        return self.factories[idx][1].prepare(quantity)



def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(200)
    elif type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None


if __name__ == '__main__':

    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()
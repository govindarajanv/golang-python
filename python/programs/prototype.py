import copy

class Car:
    """ Car prototype """

    def __init__(self):
        self.__engine = "3000cc"
        self.__model = "prototype"
        self.__color = "Red"
        self.__seats = 5
        self.__type = "Hatchback"

    def __str__(self):
        return f"Car model: {self.__model} with engine: {self.__engine}, color: {self.__color}, seats: {self.__seats}, type: {self.__type}"

class PrototypeFactory:


    def __init__(self):
        self.__instances = {}

    def registerObject(self,name,obj):
        self.__instances[name] = obj

    def unregisterObject(self,name):
        del self.__instances[name]


    def clone(self,name,**kwargs):
        clonedObject = copy.deepcopy(self.__instances[name])
        # this is also very important in addition to deepcopy
        clonedObject.__dict__.update(kwargs)
        return clonedObject

if __name__ == "__main__":
    car = Car()
    
    prototypeFactory = PrototypeFactory()

    prototypeFactory.registerObject('basicCar',car)

    i10 = prototypeFactory.clone("basicCar",_Car__model="i10")
    print (i10)
    creta = prototypeFactory.clone("basicCar",_Car__color="Blue",_Car__type="SUV",_Car__model="Creta")
    print (creta)





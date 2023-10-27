import copy

class Car:
    """ Car prototype """

    def __init__(self):
        self.__engine_no = None
        self.engine = "1100cc"
        self.make = "Maruti"
        self.model = "prototype" # this is important
        self.variant = None
        
    def __str__(self):
        return f"{self.__class__.__name__}/ {self.__engine_no}/ {self.engine}/  {self.make} / {self.model} / {self.variant}"
    
class PrototypeBodyBuildingFactory:
    
    def __init__(self):
        self.__instances = {}
        
    def registerObject(self,name, obj):
        self.__instances[name] = obj

    def deregisterObject(self,name):
        del self.__instances[name]
        
    def clone(self,name,**kwargs):
        clonedObject = copy.deepcopy(self.__instances[name])
        # this is also very important in addition to deepcopy
        clonedObject.__dict__.update(**kwargs)
        return clonedObject
        
if __name__ == "__main__":
    
    chassis = Car()
    
    pf = PrototypeBodyBuildingFactory()
    pf.registerObject("hatchback",chassis)
    car1 = pf.clone("hatchback",variant="Petrol",_Car__engine_no="12345",model="Swift")
    #print (car1)
    car2 = pf.clone("hatchback",variant="Diesel",_Car__engine_no="12346",model="Ritz")
    print (car1, car2,sep="\n")
    pf.deregisterObject("hatchback")
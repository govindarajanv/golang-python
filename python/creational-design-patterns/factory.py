class Tea:
    
    def __init__(self,qty,type):
        self.type = type
        self.qty = qty
        
    def __str__(self):
        return f"{self.type} {self.__class__.__name__} with qty {self.qty} is served"
        
    def consume(self):
        print (f"{self.type} {self.__class__.__name__} with qty {self.qty} is consumed")

class TeaFactory:
    
    @staticmethod
    def prepare(qty,type="Normal"):
        return Tea(qty,type)
        
if __name__ == "__main__":
    mug1 = TeaFactory.prepare(200)
    print (mug1)
    mug1.consume()
    
    mug2 = TeaFactory.prepare(150,"Elaichi")
    print (mug2)
    mug2.consume()
class Tea:
    
    def __init__(self,flavor,qty):
        self.flavor = flavor
        self.qty = qty
        
    def __str__(self):
        return f"{self.flavor} {self.__class__.__name__} with qty {self.qty} is ordered"
        
    def serve(self):
        print (f"{self.flavor} {self.__class__.__name__} with qty {self.qty} is served")

class TeaFactory:
    
    @staticmethod
    def order(flavor="Plain",qty="200"):
        return Tea(flavor,qty)
        
if __name__ == "__main__":
    order1 = TeaFactory.order()
    print (order1)
    order1.serve()
    
    order2 = TeaFactory.order("Elaichi",150)
    print (order2)
    order2.serve()

"""

Generate documentation using pydoc as follows

python3 -m pydoc -w ./dunder.py 
"""


class Dunder:
    def __new__(cls,name)->object:
        print ("__new__ is called")
        return super(Dunder, cls).__new__(cls)

    def __init__(self,name)->None:
        print (f"__init__ is called with {name} as the argument")
        self.__name = name


    def __str__(self)->str:
        print ("__str__ is called")
        return f"Class Dunder with {self.__name}. Returned by __str__"

    def __repr__(self)->str:
        print ("__repr__ is called but will be overridden by __str__")
        return f"Class Dunder with {self.__name}. Returned by __repr__"

    def __call__(self,times,*args, **kwargs)->None:
        print ("__call__ is called")
        print (f"{self.__name} " * times)

    @property
    def __dict__(self)->str:
        print ("__dict__ is called")
        return {"name": self.__name}

    def __del__(self)->None:
        print (f"__del__ is called for {self.__name}")

if __name__ == "__main__":
    d1 = Dunder("Magic")
    print (d1)
    d1(3)
    print ("=" * 50)
    d2 = object.__new__(Dunder)
    d2.__init__("New")
    print (d2.__dict__)

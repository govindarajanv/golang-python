class Dunder:

    # Add type hint
    def __new__(cls,*args, **kwargs):
        print ("__new__ is called")
        instance = super(Dunder,cls).__new__(cls)
        return instance

    def __init__(self,name) -> None:
        print ("__init__ is called")
        self.__name = name

    def __str__(self) -> str:
        print ("__str__ is called")
        return self.__name

    def __del__(self,*args, **kwargs) -> None:
        print ("__del is called")

    def __call__(cls, *args, **kwargs):
        print ("__call__ is called")

if __name__ == "__main__":
    d1 = Dunder('python')
    print (d1)
    d1()

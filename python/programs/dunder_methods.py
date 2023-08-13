"""

Generate documentation using pydoc as follows

python3 -m pydoc -w ./dunder.py 
"""


class Dunder:

    """
    class method to create a new instance
    """

    def __new__(cls, name, tag) -> object:
        print("__new__")
        return super(Dunder, cls).__new__(cls)

    """
			instance method to initialize a new instance
		"""

    def __init__(self, name, tag) -> None:
        print("__init__")
        self.name = name
        self.tag = tag

    """
			instance method to stringify the object which is humanreadable
		def __str__(self)->str:
				print ("__str__ return string value of class name")
				return self.name

			instance method to string representation the object
	"""

    def __repr__(self) -> str:
        print("__repr__ return string value of class name as shown below  and it is called by __str__")
        return f" Dunder class with {self.name}"

    @property
    def __dict__(self):
        print("__dict__")
        return {"name": self.name}

    """
    _call__ method helps to make instance call behave like functions

    """

    def __call__(self, times):
        print("__call__")
        print(f"{self.name} " * times)

    """
    _del__ method gets executed whenever an object is deleted
    """

    def __del__(self):
        print("__del__")


if __name__ == "__main__":
    d1 = Dunder("Testing", "magic")
    print ("calling an object with parameters")
    d1(3)

    print("-----------------------")

    d2 = object.__new__(Dunder)
    d2.__init__("Python", "magic")
    print(d2.__dict__)
    print(d2)

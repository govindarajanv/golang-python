class Database:

    __shared_state = {}

    def __init__(self,name):
        self.__dict__ = self.__shared_state
        self.name = name


if __name__ == "__main__":

    d1 = Database("postgres")
    d2 = Database("mysql")

    print (d1==d2)
    print (d1.__dict__)
    print (d2.__dict__)
    print(d1.__dict__ == d2.__dict__) 
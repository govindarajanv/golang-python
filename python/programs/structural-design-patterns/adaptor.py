class MobileAdapter:
    def __init__(self):
        self.out_voltage = 0
        self.out_ampere = 0

    def connect(self)

class  Socket:
    pass

class Mobile:
    def __init__(self):
        self.__charging = False
        self.__voltage = 5
        self.__ampere = 2.1

    def connect(self,adapter):
        if adapter.out_voltage == self.__voltage and adapter.out_ampere == self.__ampere:
            self.__charging = True
        else:
            self.__charging = False

    def charge_status(self):
        return self.__charging


if __name__ == "__main__":
    mobile = Mobile()
    adapter = MobileAdapter()
    mobile.connect(adapter)
    print (mobile.charge_status())

class MobileAdapter:
    def __init__(self):
        self.out_voltage = 0
        self.out_ampere = 0

    def deliver(self,in_voltage,in_ampere):
        if in_voltage == 220:
            self.out_voltage = 5
        else:
            self.out_voltage = 0
        if in_ampere == 5:
            self.out_ampere = 2.1
        else:
            self.out_ampere = 0


class  Socket:
    def __init__(self):
        self.adapter = None
        self.switched_on = False

    def connect(self,adapter):
        self.adapter = adapter

    def switch_on(self):
        self.switched_on = True
        if self.adapter:
            self.adapter.deliver()
    def switch_off(self):
        self.switched_on = False
        if self.adapter:
            self.adapter.in_voltage = 0
            self.adapter.in_ampere = 0


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

    socket = Socket()

    mobile = Mobile()
    adapter = MobileAdapter()
    socket.connect(adapter)
    mobile.connect(adapter)
    print (mobile.charge_status())

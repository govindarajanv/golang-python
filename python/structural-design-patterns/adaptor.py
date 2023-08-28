class MobileAdapter:
    def __init__(self):
        self.out_voltage = 0
        self.out_ampere = 0

    def transform(self,in_voltage,in_ampere):
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

    def connect(self,adapter):
        self.adapter = adapter

    def power_on(self):
        if self.adapter:
            self.adapter.transform(220,5)
    def power_off(self):
        if self.adapter:
            self.adapter.transform(0,0)

class Mobile:
    def __init__(self):
        self.adapter = None
        self.__voltage = 5
        self.__ampere = 2.1
        self.__charging = False

    def connect(self,adapter):
        self.adapter = adapter

    def charge_status(self):
        if self.adapter.out_voltage == self.__voltage and self.adapter.out_ampere == self.__ampere:
            self.__charging = True
        else:
            self.__charging = False
        return f"\n-> Mobile charging: {self.__charging}\n"

if __name__ == "__main__":

    socket = Socket()

    mobile = Mobile()

    adapter = MobileAdapter()

    mobile.connect(adapter)
    print ("mobile connected to adapter")

    socket.connect(adapter)
    print ("socket connected to adapter")

    print (mobile.charge_status())

    socket.power_on()
    print ("socket is powered on")

    print (mobile.charge_status())

    socket.power_off()
    print ("socket is powered off")

    print (mobile.charge_status())


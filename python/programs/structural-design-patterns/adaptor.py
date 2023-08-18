class TypeA_Plug:

    def __init__(self):
        self.current = "15 A"
        self.voltage = "110 V"
    
    def connect(self,socket):
        ret = True
        if (self.current != socket.current or self.voltage != socket.voltage):
            ret = False
        return ret 

    def deliver(self):
        return self.current, self.voltage

    def __str__(self):
        return f"Plug Type A ({self.current}/{self.voltage})\n"

class TypeA_Socket:

    def __init__(self):
        self.current = "15 A"
        self.voltage = "110 V"
    
    def deliver(self,plug):
        self.current = current
        self.voltage = voltage

    def __str__(self):
        return f"Socket Type A ({self.current}/{self.voltage})\n"

class TypeC_Socket:
    
    def __init__(self):
        self.current = "2.5 A"
        self.voltage = "220 V"
    
    def deliver(self,plug):
        self.current = current
        self.voltage = voltage

    def __init__(self):
        self.current = "2.5 A"
        self.voltage = "220 V"
    
    def deliver(self,plug):
        self.current = current
        self.voltage = voltage

    def __str__(self):
        return f"Socket Type C ({self.current}/{self.voltage})\n"

class C2AAdapter:

    def __init__(self):
        self.socket = "Type C"

    
class Mobile:

    def __init__(self, battery_percent):
        self.battery_percent = battery_percent
    
    def charge_me(self,plug,socket):
        print ("We are charging a mobile having battery {}%  with {} and {}\n".format(self.battery_percent,plug,socket))
        if plug.connect(socket):
            self.battery_percent = str(int(self.battery_percent) + 1)
            return f"Charging!!! Battery {self.battery_percent}%\n"
        else:
            return f"Not Charging!!! Battery {self.battery_percent}%\n"


if __name__ == "__main__":
    
    mobile = Mobile("10")
    plug = TypeA_Plug()
    socket = TypeA_Socket()
    print (mobile.charge_me(plug,socket))

    mobile = Mobile("20")
    plug = TypeA_Plug()
    socket = TypeC_Socket()
    print (mobile.charge_me(plug,socket))
    
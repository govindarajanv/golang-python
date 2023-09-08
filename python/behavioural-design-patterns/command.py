from abc import ABC,abstractmethod

class Device :
    @abstractmethod
    def on(self) :
        pass

    @abstractmethod
    def off(self) :
        pass

class Light(Device) :
    def on(self) :
        print("Turn on light")
        
    def off(self) :
        print("Turn off light")

class Speaker(Device) :
    def on(self) :
        print("Turn on speaker")
        
    def off(self) :
        print("Turn off speaker")

class Command :
    def execute(self) :
        pass

class OnCommand(Command) :

    def __init__(self, device) :
        self.device = device
        
    def execute(self) :
        self.device.on()

class OffCommand(Command) :
    
    def __init__(self, device) :
        self.device = device
        
    def execute(self) :
        self.device.off()

class Remote :
   
    def __init__(self, onCommand,  offCommand) :
        self.onCommand = onCommand
        self.offCommand = offCommand

        
    def clickOn(self) :
        self.onCommand.execute()
        
    def clickOff(self) :
        self.offCommand.execute()

if __name__=="__main__":
    
    tableLight = Light()
    portableSpeaker = Speaker()
    
    remote1 = Remote(OnCommand(tableLight),OffCommand(tableLight))
    remote1.clickOn()
    remote1.clickOff()

    remote2 = Remote(OnCommand(portableSpeaker), OffCommand(portableSpeaker))
    remote2.clickOn()
    remote2.clickOff()
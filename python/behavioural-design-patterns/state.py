# an object alter its behavior when its internal state changes
from abc import ABC, abstractmethod

class NotificationMode(ABC):
    
    @abstractmethod
    def check(self, ctx):
        pass

class Vibration(NotificationMode):
    def check(self, ctx):
        print("Phone will vibrate")
        
class Silent(NotificationMode):
    def check(self, ctx):
        print("Notifications will be silenced")

class Ring(NotificationMode):
    def check(self, ctx):
        print("Phone will ring")
        
# context
class AlertSetting:
    def __init__(self):
        self.currentState = Ring()

    def setState(self, state):
        self.currentState = state

    def check(self):
        self.currentState.check(self)

if __name__ == "__main__":
    setting = AlertSetting()
    setting.check()
    setting.setState(Vibration())
    setting.check()
    setting.setState(Silent())
    setting.check()

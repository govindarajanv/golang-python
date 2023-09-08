class Memento:
    def __init__(self, state):
        self.state = state
    
    def getState(self):
        return self.state

class Originator:
    def __init__(self):
        self.state = None

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def saveStateToMemento(self):
        return Memento(self.state)

    def getStateFromMemento(self, memento):
        self.state = memento.getState()

class CareTaker:
   def __init__(self):
      self.mementoList = []

   def add(self, state):
      self.mementoList.append(state)

   def get(self, index):
      return self.mementoList[index]

if __name__ == "__main__":
    originator = Originator()
    careTaker = CareTaker()
    originator.setState("State #1")
    originator.setState("State #2")
    careTaker.add(originator.saveStateToMemento())
    originator.setState("State #3")
    careTaker.add(originator.saveStateToMemento())
    originator.setState("State #4")
    print("Current State: " + originator.getState())      
    originator.getStateFromMemento(careTaker.get(0))
    print("First saved State: " + originator.getState())
    originator.getStateFromMemento(careTaker.get(1))
    print("Second saved State: " + originator.getState())
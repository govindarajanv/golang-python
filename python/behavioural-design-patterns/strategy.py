# define a family of algorithms, put each of them into a separate class, and make their objects interchangeable
from abc import ABC, abstractmethod

class DeploymentStrategy(ABC):
    @abstractmethod
    def deploy(self, amount):
        pass


class CanaryDeployment(DeploymentStrategy):
    def deploy(self, app):
        print (f"{app} is being deployed using {self.__class__.__name__} strategy")

class BlueGreenDeployment(DeploymentStrategy):
    def deploy(self, app):
        print (f"{app} is being deployed using {self.__class__.__name__} strategy")


class RecreateDeployment(DeploymentStrategy):
    def deploy(self, app):
        print (f"{app} is being deployed using {self.__class__.__name__} strategy")

class CDTool:
    
    def __init__(self,strategy=RecreateDeployment()):
        self.__strategy = strategy

    
    def changeStrategy(self,strategy):
        self.__strategy = strategy
        
    def deploy(self,app):
        self.__strategy.deploy(app)

if __name__ == "__main__":
    spinnaker = CDTool()

    app1 = "notification-service"
    spinnaker.deploy(app1)
    
    app2 = "indexing-service"
    spinnaker.changeStrategy(CanaryDeployment())
    spinnaker.deploy(app2)
    
    app3 = "wallet-service"
    spinnaker.changeStrategy(BlueGreenDeployment())
    spinnaker.deploy(app3)
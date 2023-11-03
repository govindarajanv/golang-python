from abc import ABC,abstractmethod

class Manifest(ABC):
    @abstractmethod
    def apply(self):
        pass
    
    def __init__(self,name):
        self.name = name

class Pod(Manifest):

    def apply(self):
        return f"Pod {self.name} is applied"

    def get(self):
        return f"pod {self.name} status"

class ConfigMap(Manifest):

    def apply(self):
        return f"ConfigMap {self.name} is applied"

    def get(self):
        return f"ConfigMap {self.name} status"

class KubeCluster(ABC):
    @abstractmethod
    def apply(self,manifest):
        pass
    @abstractmethod
    def get(self,manifest):
        pass
    
class Minikube(KubeCluster):

    def apply(self,manifest):
        print (manifest.apply(),f"on {__class__.__name__}")

    def get(self,manifest):
        print (manifest.get(),f"from {__class__.__name__}")

class EKS(KubeCluster):

    def apply(self,manifest):
        print (manifest.apply(),f"on {__class__.__name__}")

    def get(self,manifest):
        print (manifest.get(),f"from {__class__.__name__}")

if __name__ == "__main__":
    pod1 = Pod("nginx")
    cm1 = ConfigMap("app1-properties")
    cluster1 = Minikube()
    cluster2 = EKS()
    
    cluster1.apply(pod1)
    cluster1.get(pod1)
    
    cluster2.apply(cm1)
    cluster2.get(cm1)

    cluster2.apply(pod1)
    cluster2.get(pod1)
    
    cluster1.apply(cm1)
    cluster1.get(cm1)  
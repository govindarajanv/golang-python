from abc import ABC,abstractmethod

class Manifest(ABC):
    @abstractmethod
    def apply(self):
        pass
    
    @abstractmethod
    def status(self):
        pass

class Pod(Manifest):
    def apply(self):
        print ("Pod configured")
    
    def status(self):
        return "kubectl get pod pod1"

class ConfigMap(Manifest):
    def apply(self):
        print ("ConfigMap configured")
    
    def status(self):
        return "kubectl get cm <cm1>"

class K8sCluster(ABC):
    
    @abstractmethod
    def kubectl_apply(self):
        pass
    
    def kubectl_get(self):
        if self.manifest:
            print ("from",self.__class__.__name__,":",self.manifest.status())
        

class EKS(K8sCluster):
    def __init__(self):
        self.manifest = None
        
    def kubectl_apply(self,manifest):
        self.manifest = manifest
        self.manifest.apply()

class Minikube(K8sCluster):
    
    def __init__(self):
        self.manifest = None
        
    def kubectl_apply(self,manifest):
        self.manifest = manifest
        self.manifest.apply()
        
if __name__ == "__main__":
    pod1 = Pod()
    cm1 = ConfigMap()
    cluster1 = EKS()
    cluster2 = Minikube()
    
    cluster1.kubectl_apply(pod1)
    cluster1.kubectl_get()
    
    cluster2.kubectl_apply(pod1)
    cluster2.kubectl_get()

    cluster1.kubectl_apply(cm1)
    cluster1.kubectl_get()
    
    cluster2.kubectl_apply(cm1)
    cluster2.kubectl_get()

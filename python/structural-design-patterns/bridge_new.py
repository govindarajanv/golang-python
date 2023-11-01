from abc import ABC,abstractmethod

class Manifest(ABC):
    
    @abstractmethod
    def apply(self):
        pass
    
    @abstractmethod
    def status(self):
        pass
    
class Pod(Manifest):
    
    def __init__(self,name):
        self.manifest_name = name
    
    def apply(self):
        return "Pod config is applied successfully"
        
    def status(self):
        return "kubectl get pod"

class ConfigMap(Manifest):
    
    def __init__(self,name):
        self.manifest_name = name
    
    def apply(self):
        return "ConfigMap config is applied successfully"
        
    def status(self):
        return "kubectl get cm"
        
class KubernetesCluster(ABC):
    
    @abstractmethod
    def kubectl_apply(self):
        pass
    
    @abstractmethod
    def kubectl_get(self):
        pass
    
class EKS(KubernetesCluster):
    
    def kubectl_apply(self,manifest):
        return manifest.apply() + " on " + self.__class__.__name__
            
    def kubectl_get(self,manifest):
        return f"{manifest.status()} {manifest.manifest_name} on EKS"
            
class Minikube(KubernetesCluster):
    
    def kubectl_apply(self,manifest):
        return manifest.apply() + " on " + self.__class__.__name__
            
    def kubectl_get(self,manifest):
        return f"{manifest.status()} {manifest.manifest_name} on Minikube"
            
if __name__ == "__main__":
    pod1 = Pod("pod1")
    cm1 = ConfigMap("cm1")
    
    mk = Minikube()
    eks = EKS()
    
    print (mk.kubectl_apply(pod1))
    print (eks.kubectl_apply(cm1))
    print (eks.kubectl_apply(pod1))
    print (mk.kubectl_apply(cm1))
    print (mk.kubectl_get(pod1))
    print (eks.kubectl_get(cm1))
    
        
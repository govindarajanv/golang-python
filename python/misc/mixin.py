from abc import ABC,abstractmethod

class EqualityMixin:
    def __eq__(self,other):
        if not isinstance(other,type(self)):
            return False
        for key in self.__dict__:
            if key != '_Deployment__name':
                if self.__dict__[key] != other.__dict__[key]:
                    return False
        return True

class K8sObject(ABC):
    
    @abstractmethod
    def __str__(self):
        pass
    
class Deployment(K8sObject,EqualityMixin):
    def __init__(self,name,image,replicas):
        self.__name = name
        self.__image = image
        self.__replicas = replicas
    def __str__(self):
        return f"{self.__name},{self.__image},{self.__replicas}"

class Daemonset(K8sObject,EqualityMixin):
    def __init__(self,name,image):
        self.__name = name
        self.__image = image

    def __str__(self):
        return f"{self.__name},{self.__image}"
        
if __name__ == "__main__":
    dp1 = Deployment("nginx","nginx:latest",2)
    dp2 = Deployment("nginx","nginx:latest",2)
    
    dms1 = Daemonset("cloudwatch","amazon/cloudwatch-agent:latest")
    dms2 = Daemonset("cloudwatch","amazon/cloudwatch-agent:different")
    
    print (dp1 == dp2, dms1 == dms2)
# defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure
from abc import ABC, abstractmethod

class Observability(ABC):
    
    @abstractmethod
    def capture(self):
        pass
    
    @abstractmethod
    def publish(self):
        pass
    
    @abstractmethod
    def view(self):
        pass
    
    # template method 
    def manage(self):
        self.capture()
        self.publish()
        self.view()
    
class Metric(Observability):
    
    def capture(self):
        print (f"{self.__class__.__name__} is captured using an OTEL collector")
        
    def publish(self):
        print (f"{self.__class__.__name__} is published to Prometheus")
        
    def view(self):
        print (f"{self.__class__.__name__} is viewed on Grafana\n") 
        
class Log(Observability):
    
    def capture(self):
        print (f"{self.__class__.__name__} is captured using Fluentd")
        
    def publish(self):
        print (f"{self.__class__.__name__} is published to Loki")
        
    def view(self):
        print (f"{self.__class__.__name__} is viewed on Grafana\n")
        
class Trace(Observability):
    
    def capture(self):
        print (f"{self.__class__.__name__} is captured using an OTEL collector")
        
    def publish(self):
        print (f"{self.__class__.__name__} is published to Jaegar")
        
    def view(self):
        print (f"{self.__class__.__name__} is viewed on Grafana\n") 
        
if __name__ == "__main__":
    cpu_usage = Metric()
    app_log = Log()
    api_trace = Trace()
    
    cpu_usage.manage()
    app_log.manage()
    api_trace.manage()
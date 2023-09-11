# define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing
class Subscriber:
    
    def __init__(self, name):
        self.name = name
        
    def notify(self,topic, *args):
        print (f"{self.name} got", args,"from",topic.name)
        
class SNSTopic:
    
    def __init__(self,name):
        self.__name = name
        self.__subscribers = []
    
    @property    
    def name(self):
        return self.__name
        
    def subscribe(self,subscriber):
        self.__subscribers.append(subscriber)
        
    def unsubscribe(self,subscriber):
        self.__subscribers.remove(subscriber)
        
    def notify_subscribers(self, *args):
        for subs in self.__subscribers:
            subs.notify(self,args)
if __name__ == "__main__":
    topic1 = SNSTopic("topicA")
    topic2 = SNSTopic("topicB")
    
    sqs1 = Subscriber("sqsA")
    lambda1 = Subscriber("lambdaA")
    
    topic1.subscribe(sqs1)
    topic1.subscribe(lambda1)
    
    topic2.subscribe(lambda1)
    
    topic1.notify_subscribers("Broadcast 1:Processing is completed")
    topic2.notify_subscribers("Broadcast 2:Processing is completed")
    
    topic1.unsubscribe(lambda1)
    print (topic1.name, "unsubscribed by", lambda1.name)

    topic1. notify_subscribers("Broadcast 3: Processing failed")
    topic2. notify_subscribers("Broadcast 4: Processing failed")
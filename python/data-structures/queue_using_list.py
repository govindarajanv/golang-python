class Queue:
    
    def __init__(self):
        self.__items = []

    def __len__(self):
        return len(self.__items)
        
    def __str__(self):
        return str(self.__items)
        
    def isEmpty(self):
        return len(self) == 0
        
    def peek(self):
        if self.isEmpty():
            raise Exception("peek() called on an empty queue")
        return self.__items[0]
    
    def enqueue(self,item):
        self.__items.append(item)
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Dequeue() called on an empty queue")
        return self.__items.pop(0)
    
        
if __name__ == "__main__":
    queue1 = Queue()
    queue1.enqueue(8)
    queue1.enqueue(10)
    print (queue1)
    print ("Queue has",len(queue1),"item")
    print ("peeking:",queue1.peek())
    print("dequeue:",queue1.dequeue())
    print ("peeking:",queue1.peek())
    print("dequeue:",queue1.dequeue())
    #print ("peeking:",queue1.peek())
    #print("dequeue:",queue1.dequeue())
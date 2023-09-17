# operations top, peek, size, isEmpty, push and pop
class Stack:
    
    def __init__(self):
        self.__items = []
        self.__top = None
    
    def __len__(self):
        return len(self.__items)
        
    def isEmpty(self):
        return len(self) == 0        
    
    def top(self):
        return len(self) - 1
            
    def peek(self):
        if self.isEmpty():
            raise Exception("peek() called on empty stack.")
        return self.__items[self.top()]
    
    def push(self,value):
        self.__items.append(value)
    
    def pop(self):
        if self.isEmpty():
            raise Exception("pop() called on empty stack.")
        return self.__items.pop()
        
    def __str__(self):
        return str(self.__items)
if __name__ == "__main__":
    stack1 = Stack()
    print ("Is Stack Empty?", stack1.isEmpty())

    stack1.push(8)
    stack1.push(4)
    print ("let us push items into stack")
    print ("now, stack contains:", stack1)
    print ("size:",len(stack1))
    print ("peek:",stack1.peek())
    print ("popping:",stack1.pop())    
    print ("top:",stack1.top())
    print ("peek:",stack1.peek())
    print ("popping:",stack1.pop())
    print ("size:",len(stack1))


    
class Node:
    
    def __init__(self,data = None):
        self.data = data
        self.next = None
        
    def set_next(self,node):
        self.next = node
        
    def __repr__(self):
        return str(self.data)
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
        
    def __str__(self):
        value = ""
        for node in self:
            value += str(node.data) + "-->"
        return value
        
    def prepend(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node 
        else:
            node.next = self.head
            self.head = node
    
    def append(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node 
            return
        else:
            # traverse the list
            for curr in self:
                pass # this takes node_ref to the end
            last_node = curr
            last_node.next = node
            
    def insert(self,node,pos):
        for node_ref in self:
            pass
        
    def reverse(self):
        prev_node = None
        curr = self.head 
        while curr:
            next_node = curr.next 
            curr.next = prev_node 
            prev_node = curr 
            curr = next_node git 
        self.head = prev_node
            
        
if __name__ == "__main__":
    
    ll = LinkedList()
    ll.append(5)
    ll.append(7)
    ll.append(10)
    print ("LinkedList:",ll)  
    ll.prepend(12)  
    print ("LinkedList:",ll)  
    ll.reverse()
    print ("LinkedList:",ll)   
    
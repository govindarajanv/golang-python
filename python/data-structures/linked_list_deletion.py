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

    def __len__(self):
        length = 0
        for curr in self:
            length += 1
        return length

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
            
    def insert(self,data,pos):
        if pos > len(self):
            raise Exception ("Index out of range")
        if pos == 0:
            self.prepend(data)
            return
        elif pos == len(self):
            self.append(data)
            return

        node = Node(data)
        index = 0
        for iter in self:
            if pos-1 == index:
                curr_node = iter
                next_node = iter.next
                curr_node.next = node                
                node.next = next_node
                return
            else:
                index += 1
        return
       
    def reverse(self):
        prev_node = None
        curr = self.head 
        while curr:
            next_node = curr.next 
            curr.next = prev_node 
            prev_node = curr 
            curr = next_node 
        self.head = prev_node

    def delete(self,pos): 

        if self.head is None:
            return

        if pos >= len(self):
            raise Exception ("Index out of range")

        temp = self.head

        if pos == 0:
            self.head = temp.next
            temp = None
            return

        index = 0
        for iter in self:
            if pos-1 == index:
                curr_node = iter
                next_node = iter.next
                curr_node.next = next_node.next                
                next_node.next = None
                return
            else:
                index += 1
        return
    def search(self,data):
        index = 0
        for iter in self:
            index += 1
            if iter.data == data:

                print (f"{data} is found at  position {index} or index of {index-1}")
                return True
            
        print (f"{data} is not found")
        return False

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
    ll.insert(17,0)
    print ("LinkedList:",ll) 
    ll.insert(11,5)
    print ("LinkedList:",ll) 
    ll.insert(24,2)
    print ("LinkedList:",ll) 
    ll.delete(3)
    print ("LinkedList:",ll) 
    ll.delete(0)
    print ("LinkedList:",ll) 
    ll.delete(4)
    print ("LinkedList:",ll) 
    ll.search(5)
    ll.search(17)
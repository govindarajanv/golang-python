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
        value = []
        for i in self:
            value.append(i.data)
        return str(value)
        
    def prepend(self,node):
        if self.head is None:
            self.head = node 
        else:
            node.next = self.head
            self.head = node
    
    def append(self,node):
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
        curr = self.head
        prev_node = None
        next_node = None
        while curr:

            next_node = curr.next # 7
            curr.next = prev_node # 11
            prev_node = curr # 5
            curr = next_node # 7
            curr = next_node
            
        
if __name__ == "__main__":
    
    ll = LinkedList()
    node1 = Node(5)
    node2 = Node(7)
    ll.head = node1
    node1.set_next(node2)
    print ("LinkedList:",ll)
    
    
    # prepend
    node3 = Node(11)
    ll.prepend(node3)
    print ("After prepending:",ll)
    
    # append
    node4 = Node(12)
    ll.append(node4)
    print ("After appending:",ll)
    
    # insert
    node5 = Node(15)
    ll.insert(node5,3)
    
    # find element
    # delete a node
    # sort list in ascending order
    # length of LinkedList
    
    
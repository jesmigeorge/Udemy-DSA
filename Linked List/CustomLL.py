from random import randint
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None
     
    #to make the node printable
#str is standard method that gives string representation of any object
#when we call the print() on the node it will print the value 
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self,values = None):
        self.head = None
        self.tail = None
        
    #to make LL iterable
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next
        
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)
    
    #built-in len() implementation for LL
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result +=1
            node = node.next
        return result
    
    #to add elements to the end of a LL
    def add(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        return self.tail
  
  
  #to call a function from another function
  #when both of them belong to the same class 
  #use self.functionName() 
    def generate(self,n,min_value,max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value,max_value))
        return self
            
customLL = LinkedList()
customLL.generate(10,0,99)
#print(customLL)
#print(len(customLL))    
    

        
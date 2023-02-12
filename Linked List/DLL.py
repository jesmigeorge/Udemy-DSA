class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def createDLL(self,nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
    
    def insertNode(self,nodeValue,location):
        if self.head is None:
            print("The node cannot be inserted")
        else:
            newNode = Node(nodeValue)
            if location==0:
                newNode.next = self.head
                newNode.prev = None
                self.head.prev = newNode
                self.head = newNode
            elif location==1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index=1
                while index<location-1:
                    tempNode = tempNode.next
                    index+=1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next.prev = newNode
                tempNode.next = newNode
                       
        
dlst = doublyLinkedList()
dlst.createDLL(32)
print([node.value for node in dlst])

#to insert to a DLL
dlst.insertNode(32,0)
dlst.insertNode(45,1)
dlst.insertNode(72,1)
print([node.value for node in dlst])
dlst.insertNode(99,3)
print([node.value for node in dlst])

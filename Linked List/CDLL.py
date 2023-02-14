class Node:
    def __init__(self,value=None):
        self.value = value
        self.prev = None
        self.next = None

class doublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail =None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
            
    def createDCLL(self,nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
    
    def insertCDLL(self,value,location):
        if self.head is None:
            print("The CDLL doesn't exist")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode 
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                currNode = self.head
                index = 1
                while index < location-1:
                    currNode = currNode.next
                    index+=1
                newNode.next = currNode.next
                newNode.prev = currNode
                newNode.next.prev = newNode
                currNode.next = newNode
    
    def traverseDCLL(self):
        if self.head is None:
            print("The DCLL is empty")
        else:
            node = self.head
            while node:
                print(node.value,end="  ")
                if node == self.tail:
                    break
                node = node.next
    
    def reverseTraversalDCLL(self):
        if self.head is None:
            print("The DCLL is empty")
        else:
            node = self.tail
            while node:
                print(node.value,end="  ")
                if node == self.head:
                    break
                node = node.prev
    
    def searchDCLL(self,key):
        if self.head is None:
            print("The DCLL is empty")
        else:
            node = self.head
            while node:
                if node.value == key:
                    return "Found the value"
                if node == self.tail:
                    return "Value doesn't exist in the DCLL"
                node = node.next
    
    def deleteNode(self,location):
        if self.head is None:
            print("The DCLL is empty")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                currNode = self.head
                index = 1
                while index < location-1:
                    currNode = currNode.next
                    index+=1
                currNode.next = currNode.next.next
                currNode.next.prev = currNode
                
    def deleteDCLL(self):
        if self.head is None:
            print("There isn't any element to delete")
        else:
            self.tail.next = None
            node = self.head
            while node:
                node.prev = None
                node = node.next
            self.head = None
            self.tail = None


dclst = doublyCircularLinkedList()
dclst.createDCLL(32)
print([node.value for node in dclst])

#to insert node in DCLL
dclst.insertCDLL(12,0)
print([node.value for node in dclst])
dclst.insertCDLL(99,1)
print([node.value for node in dclst])
dclst.insertCDLL(45,3)
print([node.value for node in dclst])

#to traverse through DCLL
dclst.traverseDCLL()
print()
#to reverse traverse through DCLL
dclst.reverseTraversalDCLL()
print()
#to search the DCLL
key = int(input("Enter value to search : "))
print(dclst.searchDCLL(key))

#to delete nodes from DCLL
print([node.value for node in dclst])
dclst.deleteNode(2)
print([node.value for node in dclst])
dclst.deleteNode(1)
print([node.value for node in dclst])
dclst.deleteNode(0)
print([node.value for node in dclst])

#to delete entire DCLL
dclst.deleteDCLL()
print([node.value for node in dclst])
# to create,insert,search,delete and traverse a circular singly linked list
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        
class circularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
        #    if node.next == self.head:
        #       break
            node = node.next
            if node == self.tail.next:
                break
    
    def createCSLL(self,nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        
    def insertCSLL(self,value,location):
        if self.head is None:
            print("The head reference is none")
        else:
            newNode = Node(value)
            # location = 0 means inserting the first element of CSLL
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            # location = 1 means inserting as the last element of CSLL
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            # location means inserting the element at location index of CSLL
            else:
                tempNode = self.head
                index = 1
                while index < location-1 :
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next 
                tempNode.next = newNode
                
    def traversalCSLL(self):
        if self.head is None:
            print("The CSLL is empty for traversal")
        else:
            node = self.head
            while node:
                print(node.value,end=' ')
                node = node.next
                if node == self.tail.next:
                    break
    
    def searchCSLL(self,key):
        if self.head is None:
            return "The CSLL is empty for search"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == key:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The node doesn't exist in CSLL"
    
    def deleteNode(self,location):
        if self.head is None:
            print("Empty CSLL")
        else:
            # location = 0 means deleting the first element of CSLL
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            # location = 1 means deleting the last element of CSLL
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            # location means deleting the element at location index of CSLL
            else:
                tempNode = self.head
                index =1 
                while index < location-1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                
    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None             
                    
clst = circularSinglyLinkedList()
clst.createCSLL(32)
print([node.value for node in clst])

#insertions to the linked list
clst.insertCSLL(45,0)
clst.insertCSLL(99,1)
print([node.value for node in clst])
clst.insertCSLL(24,2)
print([node.value for node in clst])

#traversal in CSLL
clst.traversalCSLL()

#traversal in CSLL
key = int(input("\nEnter value to search : "))
print(clst.searchCSLL(key))

#delete in CSLL
clst.deleteNode(0)
print([node.value for node in clst])
clst.deleteNode(1)
print([node.value for node in clst]) 
clst.deleteNode(2)
print([node.value for node in clst])  

#delete entire CSLL
clst.deleteEntireCSLL()
print([node.value for node in clst])  
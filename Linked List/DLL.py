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
            # location = 0 means inserting the first element of DLL
            if location==0:
                newNode.next = self.head
                newNode.prev = None
                self.head.prev = newNode
                self.head = newNode
            # location = 1 means inserting as the last element of DLL
            elif location==1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            # location = 1 means inserting as the last element of DLL
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
    
    def traverseDLL(self):
        if self.head is None:
            print("The list is empty for traversal")
        else:
            node = self.head
            while node:
                print(node.value,end=',')
                node = node.next
            print()
    
    def reverseTraversalDLL(self):
        if self.head is None:
            print("The list is empty for traversal")
        else:
            node = self.tail
            while node:
                print(node.value,end=',')
                node = node.prev
            print()
    
    def searchDLL(self,key):
        if self.head is None:
            print("The list is empty for search")
        else:
            node = self.head
            while node:
                if node.value == key:
                    print("Found")
                    break
                node = node.next
            else:
                print("Not Found")
                
    def deleteNode(self,location):
        if self.head is None:
            print("The list is empty for deletion")
        else:
            # location = 0 means deleting the first element of DLL
            if location==0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            # location = 1 means deleting the last element of DLL
            elif location==1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            # location = 1 means deleting the last element of DLL
            else:
                curNode = self.head
                index = 1
                while index < location-1:
                    curNode = curNode.next
                    index+=1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode 
    
    def deleteDLL(self):
        if self.head is None:
            print("DLL is empty")
        else:
            temp = self.head
            while temp:
                temp.prev = None
                temp = temp.next
            self.head = None
            self.tail = None
                       
        
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

# to traverse a DLL
dlst.traverseDLL()
# to reverse traverse a DLL
dlst.reverseTraversalDLL()
#to search a DLL
key = int(input("Enter value to search : "))
dlst.searchDLL(key)

#to delete a node from DLL
dlst.deleteNode(0)
dlst.deleteNode(1)
print([node.value for node in dlst])
dlst.deleteNode(2)
print([node.value for node in dlst])

#to delete entire DLL
dlst.deleteDLL()
print([node.value for node in dlst])
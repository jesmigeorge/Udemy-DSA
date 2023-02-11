#to insert,search and traverse in a singly linked list
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # to make the linked list iterable
    def __iter__(self):
        node = self.head
        while node:
           yield node
           node = node.next
    
    # to insert into the linked list 
    def insertSLL(self,value,location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
             # location = 0 means inserting the first element of SLL
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            # location = 1 means inserting as the last element of SLL
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            # location means inserting the element at location index of SLL
            else:
                tempNode = self.head
                index=1
                while index < location-1 :
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode
    
    # to traverse the linked list
    def traverseSLL(self):
        if self.head is None:
            print("The singly linked list is empty")
        else:
            node = self.head
            while node:
                print(node.value,end=' ')
                node = node.next
            print()
    
    # to search the linked list
    def searchSLL(self,key):
        if self.head is None:
            print("Value doesn't exist in the linked list")
        else:
            node = self.head
            while node:
                if node.value == key:
                    print("Value exists ")
                    break
                node = node.next
            else:
                print("Value doesn't exist in the linked list")
    
    # to delete from a linked list
    def deleteNodeSLL(self,location):
        if self.head is None:
            print("The SLL doesn't have elements to delete")
        else:
            # location = 0 means deleting the first element of SLL
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            # location = 1 means deleting the last element of SLL
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node:
                        if node.next == self.tail:
                            break
                        node = node.next
                    if node:
                        node.next = None
                        self.tail = node
            # location means deleting the element at location index of SLL
            else:
                tempNode = self.head
                index = 1
                while index < location-1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    
    #delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL doesn't exist")
        else:
            self.head = None
            self.tail = None
                
                
lst = SLinkedList()
lst.insertSLL(1,1)
lst.insertSLL(2,1)
lst.insertSLL(3,1)
lst.insertSLL(4,1)
lst.insertSLL(0,0)
lst.insertSLL(0,5)
lst.insertSLL(8,7)
print("The SLL\n")
print([node.value for node in lst])

#to perform traversal
print("SLL Traversal\n")
lst.traverseSLL()

#to perform search  
key = int(input("Enter no to search : "))
lst.searchSLL(key)     

#to perform deletion-0,1,posn
lst.deleteNodeSLL(0)
print([node.value for node in lst])
lst.deleteNodeSLL(1)
print([node.value for node in lst])
lst.deleteNodeSLL(4)
print([node.value for node in lst])

#delete the entire SLL
print("Delete the entire SLL")
lst.deleteEntireSLL()
print([node.value for node in lst])
     
    
        
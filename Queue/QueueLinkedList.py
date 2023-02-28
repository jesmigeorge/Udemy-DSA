# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 06:49:51 2023

@author: hp
"""
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def enqueue(self,value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
    
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.linkedList.head == None:
            return "Queue underflow"
        else:
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return "Dequeue done"
    
    def peek(self):
        if self.isEmpty():
            return "Empty queue"
        else:
            return self.linkedList.head
    
    def deleteQ(self):
        self.linkedList.head = None
        self.linkedList.tail = None    

customQ = Queue()
customQ.enqueue(1)
customQ.enqueue(2)
customQ.enqueue(3)
print(customQ)
print(customQ.dequeue())
print(customQ)
print(customQ.peek())
print(customQ.dequeue())
print(customQ)
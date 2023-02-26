#Q1-remove the duplicates from a given LL
from CustomLL import LinkedList

#method 1-using a temporary buffer
def removeDups(ll):
    if ll.head is None:
        return
    else:
        currNode = ll.head
        visited = set([currNode.value])
        while currNode.next:
            if currNode.next.value in visited:
                currNode.next = currNode.next.next
            else:
                visited.add(currNode.next.value)
                currNode = currNode.next
        return ll
    
def removeDups1(ll):
    if ll.head is None:
        return
    else:
        currNode = ll.head
        while currNode:
            i = currNode
            while i.next:
                if i.next.value == currNode.value:
                    i.next = i.next.next
                else:
                    i = i.next
            currNode = currNode.next
        return ll.head
                
    
custom_LL = LinkedList()
custom_LL.generate(10,0,99)
print(custom_LL)
removeDups1(custom_LL)
print(custom_LL)

#method 2-without using buffer

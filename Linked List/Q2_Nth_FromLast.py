#Q2-to print the nth last element from the given linked list

from CustomLL import LinkedList

#my method
def getNthFromLast(head,n):
    currNode = head
    k=0
    while currNode:
        k+=1
        currNode=currNode.next
    if n>k:
        return -1
    else:
        i=0
        temp = head
        while i!=(k-n):
            i+=1
            temp = temp.next
        return temp.value
    
#instructors method
def nthToLast(ll,n):
    pointer1 = ll.head
    pointer2 = ll.head
    
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

custom_LL = LinkedList()
custom_LL.generate(10,0,99)
# for i in range(5):
#     custom_LL.add(i)
# length = len(custom_LL)
# n=int(input("Enter nth from last : "))
print(custom_LL)
#print(nthToLast(custom_LL,3))
print(getNthFromLast(custom_LL.head,3))

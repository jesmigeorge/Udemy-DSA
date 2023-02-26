#Q4 : 2 nos are represented by a linked list,where 
# each node contains a single digit.The digits are stored in reverse order 
#such that the 1's digit is at head of the list.
#write a func to add 2nos and returns sum as LL.

from CustomLL import LinkedList,Node
def sumLists(ll1,ll2):
    n1 = ll1.head
    n2 = ll2.head
    ll = LinkedList()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result%10))
        carry = result // 10
    if carry!=0:
        ll.add(carry)
    # prev = LinkedList()
    # ptr = ll.head
    # while ptr:
    #     nextNode = ptr.next
    #     ptr.next =prev
    #     prev =ptr
    #     ptr = nextNode
    return ll
    
    

ll1 = LinkedList()
ll1.add(8)
ll1.add(4)
ll1.add(9)
print(ll1)
ll2 = LinkedList()
ll2.add(9)
ll2.add(2)
ll2.add(1)
print(ll2)
print(sumLists(ll1,ll2))




    
            
            
        
    
#Q3-tp partition a LL around a value x
#  such that all nodes less than x come before all node >= x
from CustomLL import LinkedList
def partition(ll,x):
    curNode = ll.head
    ll.tail = ll.head
    while curNode:
        nextNode = curNode.next
        curNode.next = None
        if curNode.value < x:
            curNode.next = ll.head
            ll.head = curNode
        else:
            ll.tail.next = curNode
            ll.tail = curNode
        curNode = nextNode
    
    if ll.tail.next is not None:
        ll.tail.next = None

custom_LL = LinkedList()
custom_LL.generate(10,0,99)
# custom_LL.add(11)
# custom_LL.add(3)
# custom_LL.add(9)
# custom_LL.add(10)
# custom_LL.add(15)
print(custom_LL)
partition(custom_LL,30) #x=30
print(custom_LL)

      
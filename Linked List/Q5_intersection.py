#Q5-given 2 singly LL,determine if they 2 intersect.return the
#intersecting node.Intersection is based on reference not value.

from CustomLL import LinkedList,Node
def intersection(ll1, ll2):
    if ll1.tail is not ll2.tail:
        return False

    lenA = len(ll1)
    lenB = len(ll2)
    shorter = ll1 if lenA < lenB else ll2
    longer = ll2 if lenA < lenB else ll1
    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head
    for i in range(diff):
        longerNode = longerNode.next
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    return longerNode

def addSmeNode(ll1, ll2,value):
    tempNode = Node(value)
    ll1.tail.next = tempNode
    ll1.tail = tempNode
    ll2.tail.next = tempNode
    ll2.tail = tempNode
    
#time complexity =O(A+B),ie,length of 2 linked lists
    
ll1 = LinkedList()
ll1.generate(3,0,10)
ll2 = LinkedList()
ll2.generate(3,0,10)
addSmeNode(ll1,ll2,11)
addSmeNode(ll1,ll2,14)
print(ll1)
print(ll2)
print(intersection(ll1,ll2))
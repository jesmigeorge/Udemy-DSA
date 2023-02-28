import QueueLinkedList as Queue
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:           # -->O(1)
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)  # -->O(n/2)
    preOrderTraversal(rootNode.rightChild)  # -->O(n/2)
    #space complexity = O(n)
    #time complexity = O(n)
    
def inOrderTraversal(rootNode):
    if not rootNode:                # -->O(1)
        return 
    inOrderTraversal(rootNode.leftChild)  # -->O(n/2)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)  # -->O(n/2)
    #space complexity = O(n)
    #time complexity = O(n)

def postOrderTraversal(rootNode):
    if not rootNode:           # -->O(1)
        return
    postOrderTraversal(rootNode.leftChild)  # -->O(n/2)
    postOrderTraversal(rootNode.rightChild)  # -->O(n/2)
    print(rootNode.data)
    #space complexity = O(n)
    #time complexity = O(n)
    
def levelOrderTraversal(rootNode):
    if not rootNode:
        return 
    else:
        customQueue = Queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

#search for a node in binary tree using 
#level order traversal as it uses queue and
#queues perform better than stack.
def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = Queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Not found"                       

print("Pre order traversal")
preOrderTraversal(newBT)
print("In order traversal")
inOrderTraversal(newBT)
print("Post order traversal")
postOrderTraversal(newBT)
print("Level order traversal")
levelOrderTraversal(newBT)
print(searchBT(newBT,"Cola"))
print(searchBT(newBT,"Hot"))
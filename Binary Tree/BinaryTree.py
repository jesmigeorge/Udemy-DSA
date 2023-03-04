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


#insertion using level order traversal to find out the first
#node that does not have any child.
#time complexity = O(n)
#space complexity = O(n)
def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = Queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully Inserted"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)           
            else:
                root.value.rightChild = newNode
                return "Successfully Inserted"

#to get the deepest node in a tree using level order traversal
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.leftChild)
        deepestNode = root.value
        return deepestNode

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return 
    else:
        customQueue = Queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)
                    
def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "The BT does not exist."
    else:
        customQueue = Queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode,dNode)
                return "The node has been successfully deleted."
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Failed to delete."
            

#to delete the binary tree as a whole         
def deleteBT(rootNode):
    rootNode.value = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The whole binary tree was deleted"    


print("Pre order traversal")
preOrderTraversal(newBT)
print("In order traversal")
inOrderTraversal(newBT)
print("Post order traversal")
postOrderTraversal(newBT)
print("Level order traversal")
levelOrderTraversal(newBT)
# print(searchBT(newBT,"Cola"))
# print(searchBT(newBT,"Hot"))
newNode = TreeNode("Tea")
print(insertNodeBT(newBT,newNode))
levelOrderTraversal(newBT)
# newNode = getDeepestNode(newBT)
# deleteDeepestNode(newBT,newNode)
# levelOrderTraversal(newBT)  
print("After deletion : ")
deleteNodeBT(newBT,'Hot')
levelOrderTraversal(newBT) 
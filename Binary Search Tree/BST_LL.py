import QueueLinkedList as queue
class BSearchTree:
    def __init__(self,value=None):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    #to insert a node
    #T(N)=O(log n) & space complexity = O(log n)
    def insertNode(self,rootNode, nodeValue):
        if rootNode.value == None:
            rootNode.value = nodeValue
        elif nodeValue <= rootNode.value:
            if rootNode.leftChild is None:
                rootNode.leftChild = BSearchTree(nodeValue)
            else:
                self.insertNode(rootNode.leftChild,nodeValue)
        else:
            if rootNode.rightChild is None:
                rootNode.rightChild = BSearchTree(nodeValue)
            else:
                self.insertNode(rootNode.rightChild,nodeValue)
        return "The node has been inserted into the tree"


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.value)
    inOrderTraversal(rootNode.rightChild)
    
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.value)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.value)
    
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.value)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

def searchNode(rootNode,nodeValue):
    flag=0
    while rootNode and flag==0:
        if rootNode.value == nodeValue:
            flag=1
        elif nodeValue < rootNode.value:
            rootNode = rootNode.leftChild
        else:
            rootNode = rootNode.rightChild
    if (flag==1):
        print("Found node")
    else:
        print("not Found node")                 
 
def deleteBST(rootNode):
    rootNode.value = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The node has been deleted successfully."

def minValueNode(rootNode):
    if rootNode:
        return 
    while rootNode.leftChild is not None:
        rootNode = rootNode.leftChild
    return rootNode.value
    
def deleteNode(rootNode,nodeValue):
    if rootNode is None:
        return
    if nodeValue < rootNode.value:
        #O(n/2)
        rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue)
    elif nodeValue > rootNode.value:
        #O(n/2)
        rootNode.rightChild = deleteNode(rootNode.rightChild,nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild #O(1)
            rootNode = None
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild #O(1)
            rootNode = None
            return temp
        
        #O(log n)
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data #O(1)
        #O(n/2)
        rootNode.rightChild = deleteNode(rootNode.rightChild.temp.data)
    return rootNode
   
newBST = BSearchTree(None)
newBST.insertNode(newBST,70)
newBST.insertNode(newBST,60)
newBST.insertNode(newBST,65)
newBST.insertNode(newBST,100)
newBST.insertNode(newBST,80)
print(newBST.value)
print(newBST.leftChild.value)
print("Preorder traversal")
preOrderTraversal(newBST)
print("Postorder traversal")
postOrderTraversal(newBST)
print("Inorder traversal")
inOrderTraversal(newBST)
print("Levelorder traversal")
levelOrderTraversal(newBST)
searchNode(newBST,65)
searchNode(newBST,68)
deleteNode(newBST,80) #space complexity = O(log n)
print("Inorder traversal")
inOrderTraversal(newBST)
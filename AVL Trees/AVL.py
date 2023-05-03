import QueueLinkedList as queue
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1
    
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
    
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
    
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue) 

#insertion
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild)-getHeight(rootNode.rightChild)

def leftRotate(disbalanceNode):
    newroot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newroot.leftChild = disbalanceNode
    disbalanceNode.height = 1+max(getHeight(disbalanceNode.leftChild),getHeight(disbalanceNode.rightChild))
    newroot.height = 1+max(getHeight(newroot.leftChild),getHeight(newroot.rightChild))
    return newroot

def rightRotate(disbalanceNode):
    newroot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newroot.rightChild = disbalanceNode
    disbalanceNode.height = 1+max(getHeight(disbalanceNode.rightChild),getHeight(disbalanceNode.leftChild))
    newroot.height = 1+max(getHeight(newroot.leftChild),getHeight(newroot.rightChild))
    return newroot


def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    rootNode.height = 1+max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance>1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance>1 and nodeValue > rootNode.rightChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return  rightRotate(rootNode)
    if balance<-1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balance<-1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode
    
#deletion    
def inorderSuccessor(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return inorderSuccessor(rootNode.leftChild)

def deleteNode(rootNode , nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = inorderSuccessor(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
        balance = getBalance(rootNode)
        if balance>1 and getBalance(rootNode.leftChild)>=0:
            return rightRotate(rootNode)
        if balance<1 and getBalance(rootNode.rightChild)<=0:
            return leftRotate(rootNode)
        if balance>1 and getBalance(rootNode.leftChild)<0:
            rootNode.leftChild = leftRotate(rootNode.leftChild)
            return rightRotate(rootNode)
        if balance<1 and getBalance(rootNode.rightChild)>0:
            rootNode.rightChild = rightRotate(rootNode.rightChild)
            return leftRotate(rootNode)
        return rootNode


#to delete entire AVLTree 
def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The AVL has been successfully deleted"

    
newAVL = AVLNode(30)
newAVL = insertNode(newAVL,25)
newAVL = insertNode(newAVL,35)
newAVL = insertNode(newAVL,20)
preOrderTraversal(newAVL)
#to delete node from AVL tree
print("Deleting node 25 from AVL tree")
deleteNode(newAVL, 25)
preOrderTraversal(newAVL)
#to delete entire AVL Tree
print("Deleting entire AVL tree")
print(deleteAVL(newAVL))
preOrderTraversal(newAVL)

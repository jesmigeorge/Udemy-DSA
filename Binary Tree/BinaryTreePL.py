class BinaryTree:
    def __init__(self,size):
        self.customList = size*[None]
        self.lastUsedIndex = 0
        self.maxSize = size
    
    def insertNode(self,value):
        if self.lastUsedIndex+1 == self.maxSize:
            return "The binary tree is full."
        self.customList[self.lastUsedIndex+1]=value
        self.lastUsedIndex+=1
        return "The value has been inserted successfully."
    
    def searchNode(self,value):
        for i in range(len(self.customList)):
            if self.customList[i] == value:
                return "Node found."
        return "Node not found."
    
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(2*index)  #---->O(n/2)
        self.preOrderTraversal(2*index+1)   #---->O(n/2)
        #so total is O(n)
    
    def inOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(2*index) #---->O(n/2)
        print(self.customList[index])
        self.inOrderTraversal(2*index+1) #---->O(n/2)
        
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(2*index)  #---->O(n/2)
        self.postOrderTraversal(2*index+1)   #---->O(n/2)
        print(self.customList[index])
        #so total is O(n)
    
    def levelOrderTraversal(self,index):
        for i in range(index,self.lastUsedIndex+1): #---->O(n/2)= Time complexity
            print(self.customList[i])
    
    def deleteNode(self,value):
        if self.lastUsedIndex == 0:
            return "No node to delete"
        for i in range(1,self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex]=None
                self.lastUsedIndex-=1
                return "Node has been deleted successfully"
    
    #to delete the entire binary tree
    def deleteBT(self):
        self.customList = None
        return "The BT has been successfully deleted"

newBT = BinaryTree(8) # a list of size 8 is created
#insertion to list if BT
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
#iterating through the BT List is same as level order traversal.
print(newBT.searchNode("Kaffe"))
print(newBT.searchNode("Hot"))
print("Inorder Traverse")
newBT.inOrderTraversal(1)
print("\nPreorder Traverse")
newBT.preOrderTraversal(1)
print("\nPostorder Traverse")
newBT.postOrderTraversal(1)
print("\nLevelorder Traverse")
newBT.levelOrderTraversal(1)
newBT.deleteNode("Cold")
print("\nPreorder Traverse")
newBT.preOrderTraversal(1)
#to delete the entire binary tree
deleteBT()
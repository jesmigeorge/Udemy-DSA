class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endOfString = True
        
    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        
        if currentNode.endOfString == True:
            return True
        else:
            return False
    
def deleteString(root, word, index):
    # case 1:  this word has the same prefix as another word
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted  = False
    
    #case 2: when the word is a prefix to some other word
    if len(currentNode.children)>1:
        deleteString(currentNode, word, index+1)
        return False
    
    if index == len(word)-1:
        if len(currentNode.children)>=1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
    
    # case 3 : when some other word is prefix to this word
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index+1)
        return False
    
    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted == True:
        return True
    else:
        return False
       
newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
print(newTrie.searchString("App"))
print(newTrie.searchString("Apie"))
deleteString(newTrie.root, "App", 0)
print(newTrie.searchString("App"))

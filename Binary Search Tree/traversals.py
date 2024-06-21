# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 10:36:30 2024

@author: hp
"""

class BST:
    def __init__(self,val=None):
        self.value = val
        self.lc = None
        self.rc = None
    
    def insertNode(self,root,val):
        if root.value==None:
            root = BST(val)
        elif val <= root.value:
            if not root.lc:
                root.lc = BST(val)
            else:
                self.insertNode(root.lc, val)
        else:
            if not root.rc:
                root.rc = BST(val)
            else:
                self.insertNode(root.rc, val)
    
    def inorder(self,root):
        if not root:
            return root
        self.inorder(root.lc)
        print(root.value,end = " ")
        self.inorder(root.rc)
    
    def search(self,root,val):
        if root.value == val:
            return root
        elif root.lc is not None and root.lc.value >= val:
            return self.search(root.lc,val)
        elif root.rc is not None and root.rc.value <= val:
            return self.search(root.rc,val)
    
    def levelorder(self,root):
        queue = [root.value]
        while queue!=[]:
            val = queue.pop(0)
            print(val)
            node = self.search(root,val)
            if not node and node.lc is not None:
                queue.append(node.lc.value)
            if not node and node.rc is not None:
                queue.append(node.rc.value)                      

tree = BST(8)
lst = [3,10,1,6,14,4,7,13]
for ele in lst:
    tree.insertNode(tree, ele)
#tree.inorder(tree)
tree.levelorder(tree)

        
    
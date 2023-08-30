'''
Interview 1 - 30 August 2023
Given an employee organization , where a node having children is a
manager.Each employee has his own salary.Find the no of managers 
who have their salary less than all of his subordinates.

                    A(10)
            B(20)          C(200)
        D(50) E(10)             F(20)
                             G(20)  H(30)

In this A and B are the managers with salary less than average 
of all the employees who has less importance than him in hierarchy.
'''

class Tree:
    def __init__(self,name,val=None):
        self.name = name
        self.value = val
        self.left = None
        self.right = None
    
    def minNum(self,node,total,cnt,minval):
        if not node.left and not node.right:
            return node.value,cnt+1,minval
        
        if (not node.left and node.right) or (node.left and not node.right):
            temp = node.left if node.left else node.right
            val,cnt,minval = self.minNum(temp,total,0,minval)
            if total//cnt > temp.value:
                minval += 1
            return val+node.value,cnt+1,minval
        
        leftval,cnt1,minval = self.minNum(node.left,total,cnt,minval)
        rightval,cnt2,minval = self.minNum(node.right,total,cnt,minval)
        total = leftval+rightval
        cnt = cnt1+cnt2
        if total//cnt > node.value:
            minval += 1
        return total+node.value,cnt+1,minval
    
root = Tree("a",10)
root.left = Tree("b",20)
root.right = Tree("c",200)
root.left.left = Tree("d",50)
root.left.right = Tree("e",10)
root.right.right = Tree("f",70)
root.right.right.left = Tree("g",20)
root.right.right.right = Tree("h",30)       
total,cnt,minval = root.minNum(root, 0, 0, 0)
print(minval)
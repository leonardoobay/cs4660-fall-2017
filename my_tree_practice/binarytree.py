class node:

def __init__(self, name, parent=-1):
    self._name = name
    self._parent = parent #paremt
    self._left = -1 #child one
    self._right = -1 #child two

def getName(self):
    return self._name

def getParent(self):
    return self._parent

def getLeft(self):
    return self._left

def getRight(self):
    return self._right

def setParent(self, p):
    self._parent = p

def setLeft(self, l):
    self._left = l

def setRight(self, r):
    self._right = r


"""A very common type of tree is called a 
binary tree. In this case, every 
node  has  no  more  than  two  children.  We’ll  usually  call  them  a  left  
child and a right child. So, a node will hold a parent, a left child, and a 
right child.""" 

"""
page 245
https://guidebookstgc.snagfilms.com/9151_ComputerScience.pdf
  
 Binary  trees  have  many  uses,  but  a  common  one  is  to  store  objects  in  
sorted order. We call these 
binary search trees
. Unlike arrays or lists that 
we might have to sort every time we add a new value, a binary tree can 
keep items always in sorted order. It’s usually faster to add an item to a 
binary tree than to add it to an array or list that’s been sorted. 

With a binary search tree, at any node in the tree, all the descendants on 
the  left  side  are  less  than  the  node,  and  all  those  on  the  right  side  are  
greater  than  the  node.  Notice,  for  example,  that  21  is  greater  than  the  
root, 15, so it’s on the right side of the root. It’s greater than the next node, 
18, so it’s also on the right side of it. But it’s less than the next node, 23, so 
it’s on the left side of that one.

"""

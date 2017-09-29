class node:

def __init__(self, name, parent=-1):
    self._name = name
    self._parent = parent
    self._children = []

def getName(self):
    return self._name

def getParent(self):
    return self._parent

def getChildren(self):
    return self._children

def setParent(self, p):
    self._parent = p


def addChild(self, c):
    self._children.append(c)

    
    """Because trees have a particular structure, they often have a particular 
way they are stored in code. Trees almost always use an adjacency list, 
where the edges are stored inside each node. And they usually store the 
parent  and  the  children  separately.  So,  any  one  node  will  store  its  own  
information, along with an index (or some other notation, such as a name) 
for the parent node, along with a list of its children. 
͸
In code, we’ll keep a variable to give the parent, and we’ll keep a list of 
variables that are the children. We can add additional children whenever 
we need to."""
    
    """page 244""
    """https://guidebookstgc.snagfilms.com/9151_ComputerScience.pdf"""

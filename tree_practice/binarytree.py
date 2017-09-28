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

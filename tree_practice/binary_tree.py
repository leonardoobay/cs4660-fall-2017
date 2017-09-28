class node:
def __init__(self, name, parent=-1):
self._name = name
self._parent = parent
self._left = -1
self._right = -1
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

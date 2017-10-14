class Node(object):
def __init__(self, data, next = None):
  self.data = data
  self.next_node = next
def get_next(self):
  return self.next_node
def set_next(self, next):
  self.next_node = next
def get_data(self):
  return self.data
def set_data(self):
  self.data = data
	
class LinkedList(object):
def __init__(self, root = None):
  self.root = root
  self.size = 0
def size(self):
  return self.size
def insert(self, data):
  new_node = Node (data, self.root)
  self.root = new_node
  self.size += 1
def delete(self, data):
  this_node = self.root
  prev_node = None
  while this_node:
    if this_node.get_data() == data:
      if prev_node:
        prev_node.set_next(this_node.get_next())
      else:
        self.root = this_node
      self.size -= 1
      return True
    else:
      prev_node = this_node
      this_node = this_node.get_next()
  return False
def search(self, data):
  this_node = self.root
  while this_node:
    if this_node.get_data() == data:
      return data
    else:
      self.root = this_node.get_next()
    return None
def printLL(self):
  this_node = self.root
  while this_node:
    print(this_node.data)
    this_node  = this_node.get_next()
	
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.printLL()
ll.delete(2)
ll.printLL()
if ll.search(2):
    print("Value 2 found")
else:
    print("Value 2 not found")
if ll.search(1):
    print("Value 1 found")
else:
    print("Value 1 not found")
ll.insert(4)
ll.printLL()
print(str(ll.size()))
	
2
1
2
1
Value 2 found
Value 1 not found
4
1
Traceback (most recent call last):
  File "C:UsersErikIngvoldsenDocumentsPython CodeTestCode.py", line 71, in <module>
    print(str(ll.size()))
TypeError: 'int' object is not callable
	
2 1
1
Value 2 not found
Value 1 found
4 1
2

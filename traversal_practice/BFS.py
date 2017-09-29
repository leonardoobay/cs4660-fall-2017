"""Let’s imagine that we have a social network, where people form the
nodes, and we have an edge connecting people if they’re friends with
each other. If we want to know the shortest way to connect two people
through a sequence of friends, we can find that out through a breadthfirst
search"""

"""
Input: A graph, a starting node, S, and a goal node, G
Output: A path of edges between G and S
1. Add information to each node:
a. Unseen/seen - initialize to "unseen"
b. Previous node in BFS - initialize to none
2. Initialize queue of nodes to visit with S, and initialize S
to "seen"
3. While goal is not found and queue is not empty:
a. Get next node in queue
b. Check all neighbors. If neighbors are "unseen":
1. Mark neighbor as "seen"
2. Set neighbor's previous node to current node
3. See if the neighbor is the goal, if so, exit the loop
4. Add this node to queue
4. If goal was found:
a. Create list of edges by following "previous node."
"""


class node:
def __init__(self, name):
self._name = name
self._friends = []
self._status = 0
self._discoveredby = 0
def isUnseen(self):
    if self._status == 0:
    return True
    else:
    return False

def isSeen(self):
    if self._status == 1:
      return True
    else:
      return False

def setUnseen(self):
    self._status = 0

def setSeen(self):
    self._status = 1

def getName(self):
  return self._name
def getFriends(self):
  return self._friends
def addFriend(self, friend_index):
  self._friends.append(friend_index)
def makeFriends(name1, name2):
  for i in range(len(people)):
    if people[i].getName() == name1:
    n1 = i
    if people[i].getName() == name2:
    n2 = i

    people[n1].addFriend(n2)
    people[n2].addFriend(n1)
def discover(self, n):
self._discoveredby = n
def discovered(self):
return self._discoveredby

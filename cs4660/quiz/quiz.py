"""
quiz2!

Use path finding algorithm to find your way through dark dungeon!

Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9

TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

"""
Preparing to push to git hub.
Test with empty files.
Attempt #1.
"""

import json
from math import sqrt

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

class List(object):
    def __init__(self):
        self.memory = []
        # we store the length separately because in real life
        # the "memory" doesn't have a length you can read from
        self.length = 0

    def get(self, address):
        return self.memory[address]

    def push(self, value):
        self.memory.insert(self.length, value)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return

        lastAddress = self.length - 1
        value = self.memory[lastAddress]
        del self.memory[lastAddress]
        self.length -= 1

        return value

    def unshift(self, value):
        # push item to beginning of the list
        previous = value

        # use enumerate to loop with index (address)
        for address, _ in enumerate(self.memory):
            current = self.memory[address]
            self.memory[address] = previous
            previous = current

        self.memory.insert(self.length, previous)
        self.length += 1

    def shift(self):
        # pop first item out of list
        if self.length == 0:
            return

        value = self.memory[0]

        # use enumerate to loop with index (address)
        for address, _ in enumerate(self.memory):
            self.memory[address] = self.memory[address + 1]

        del self.memory[self.length - 1]
        self.length -= 1

        return value

class HashTable(object):
    def __init__(self):
        self.memory = {}

    def hashKey(self, key):
        hash_token = 0
        for character in key:
            hash_token = 101 * hash_token + ord(character)
        return hash_token

    def get(self, key):
        address = self.hashKey(key)
        return self.memory[address]

    def set(self, key, value):
        address = self.hashKey(key)
        self.memory[address] = value

    def remove(self, key):
        address = self.hashKey(key)
        if address in self.memory:
            del self.memory[address]
        
        
"""
graph module defines the knowledge representations files

A Graph has following methods:

* adjacent(node_1, node_2)
    - returns true if node_1 and node_2 are directly connected or false otherwise
* neighbors(node)
    - returns all nodes that is adjacency from node
* add_node(node)
    - adds a new node to its internal data structure.
    - returns true if the node is added and false if the node already exists
* remove_node
    - remove a node from its internal data structure
    - returns true if the node is removed and false if the node does not exist
* add_edge
    - adds a new edge to its internal data structure
    - returns true if the edge is added and false if the edge already existed
* remove_edge
    - remove an edge from its internal data structure
    - returns true if the edge is removed and false if the edge does not exist
"""

from io import open
from operator import itemgetter

def construct_graph_from_file(graph, file_path):
    """
    TODO: read content from file_path, then add nodes and edges to graph object

    note that grpah object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented

    In example, you will need to do something similar to following:

    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph
    """
    f = open(file_path, 'r')
    lines = f.read().split('\n')[:-1]
    f.close()
    num_nodes = int(lines[0])
    for n in range(num_nodes):
        graph.add_node(Node(n))

    edges = []
    for edge in lines[1:]:
        start, end, weight = edge.split(':')
        start = int(start)
        end = int(end)
        weight = int(weight)
        graph.add_edge(Edge(Node(start), Node(end), weight))

    # graph.create_representation(nodes, edges)
    return graph

class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Node({})'.format(self.data)
    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data

    def __gt__(self, other_node):
        return self.data > other_node.data

    def __lt__(self, other_node):
        return self.data < other_node.data

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)

class Edge(object):
    """Edge represents basic unit of graph connecting between two edges"""
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)
    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight))


class AdjacencyList(object):
    """
    AdjacencyList is one of the graph representation which uses adjacency list to
    store nodes and edges
    """
    def __init__(self):
        # adjacencyList should be a dictonary of node to edges
        self.adjacency_list = {}

    def adjacent(self, node_1, node_2):
        if node_2 in self.neighbors(node_1):
            return True
        return False

    def neighbors(self, node):
        edges = self.adjacency_list.get(node, [])
        neighbors = [e.to_node for e in edges]
        return neighbors

    def add_node(self, node):
        if node in self.adjacency_list:
            return False
        self.adjacency_list[node] = []
        return True

    def remove_node(self, node):
        if node in self.adjacency_list:
            del self.adjacency_list[node]
            for nodes, edges in self.adjacency_list.items():
                 temp_list = []
                 for edge in edges:
                     if edge.to_node != node:
                         temp_list.append(edge)
                 self.adjacency_list[nodes] = temp_list
            return True
        return False
    
    def add_edge(self, edge):
        from_node = edge.from_node
        if edge in self.adjacency_list.get(from_node, []):
            return False
        self.adjacency_list[from_node].append(edge)
        return True
        

    def remove_edge(self, edge):
        from_node = edge.from_node
        if edge not in self.adjacency_list.get(from_node, []):
            return False
        idx = self.adjacency_list[from_node].index(edge)
        del(self.adjacency_list[from_node][idx])
        return True


    def distance(self, node_1, node_2):
        if node_1 not in self.adjacency_list:
            return None
        for edge in self.adjacency_list[node_1]:
            if edge.to_node == node_2:
                return edge
        return none


class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []

    def adjacent(self, node_1, node_2):
        node_1_idx = self.__get_node_index(node_1)
        node_2_idx = self.__get_node_index(node_2)
        if node_1_idx is False or node_2_idx is False:
            return False
        if self.adjacency_matrix[node_1_idx][node_2_idx] == 0:
            return False
        return True

    def neighbors(self, node):
        neighbors = []
        node_idx = self.__get_node_index(node)

        for idx, col in enumerate(self.adjacency_matrix[node_idx]):
            if col and idx != node_idx:
                neighbors.append(self.nodes[idx])
        return neighbors


    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            self.nodes.append(node)
            # Add a new column for all the rows
            for row in self.adjacency_matrix:
                row.append(0)
            new_row = [0 for n in self.nodes]
            self.adjacency_matrix.append(new_row)
            return True


    def remove_node(self, node):

        if node not in self.nodes:
            return False
        node_idx = self.__get_node_index(node)
        # Remove edges
        for row in self.adjacency_matrix:
            del(row[node_idx])
        
        del(self.adjacency_matrix[node_idx])
        # Remove nodes
        del(self.nodes[node_idx])
        return True


    def add_edge(self, edge):
        from_node_idx = self.__get_node_index(edge.from_node)
        to_node_idx = self.__get_node_index(edge.to_node)
        if from_node_idx is False or to_node_idx is False:
            return False
        if self.adjacency_matrix[from_node_idx][to_node_idx] != 0:
            return False
        self.adjacency_matrix[from_node_idx][to_node_idx] = edge.weight
        return True
        

    def remove_edge(self, edge):
        from_node_idx = self.__get_node_index(edge.from_node)
        to_node_idx = self.__get_node_index(edge.to_node)
        if from_node_idx is False or to_node_idx is False:
            return False
        if self.adjacency_matrix[from_node_idx][to_node_idx] == 0:
            return False
        self.adjacency_matrix[from_node_idx][to_node_idx] = 0
        return True


    def distance(self, node_1, node_2):
        node_1_idx = self.__get_node_index(node_1)
        node_2_idx = self.__get_node_index(node_2)
        
        if node_1_idx is False or node_2_idx is False:
            return None
        if self.adjacency_matrix[node_1_idx][node_2_idx] == 0:
            return None
        return Edge(node_1, node_2, self.adjacency_matrix[node_1_idx][node_2_idx])


    def __get_node_index(self, node):
         """helper method to find node index"""
         if node in self.nodes:
             return self.nodes.index(node)    

class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    def adjacent(self, node_1, node_2):
        if node_1 not in self.nodes or node_2 not in self.nodes:
            return False
        for edge in self.edges:
            if edge.from_node == node_1 and edge.to_node == node_2:
                return True
        return False   


    def neighbors(self, node):
        neighbors = []
        for edge in self.edges:
            if edge.from_node == node:
                neighbors.append(edge.to_node)
        return neighbors

    def add_node(self, node):
        if node in self.nodes:
            return False
        self.nodes.append(node)
        return True
        

    def remove_node(self, node):
        if node not in self.nodes:
            return False
        node_idx = self.nodes.index(node)
        del(self.nodes[node_idx])
        new_edges = []
        for edge in self.edges:
            if edge.to_node == node or edge.from_node == node:
                continue
            new_edges.append(edge)
        self.edges = new_edges
        return True

    def add_edge(self, edge):
        if edge in self.edges:
            return False
        if edge.from_node not in self.nodes or edge.to_node not in self.nodes:
            return False
        self.edges.append(edge)
        return True
        

    def remove_edge(self, edge):
        if edge not in self.edges:
            return False
        del(self.edges[self.edges.index(edge)])
        return True


    def distance(self, node_1, node_2):
        for edge in self.edges:
            if edge.from_node == node_1 and edge.to_node == node_2:
                return edge
        return None

        
import json
import codecs
# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.

    You will be able to get the weight of edge between two rooms using this method
    """
    # room_id


    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    #response = json.load(urlopen(req, jsondataasbytes))
    reader = codecs.getreader("utf-8")
    response = json.load(reader(urlopen(req, jsondataasbytes)))
    return response

def cost(x1, y1, x2, y2):
    return sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2))


def BFS(src, dst):  

    print ('BFS Path:')
    
    list = List()
    hashTable = HashTable()
    finalNode = None
    found = False
    
    hp = 0
    empty_room = get_state(src)
    previous = Node([empty_room['id'], '', 0, empty_room['location']['name']])
    list.push(previous)
    while list.length > 0:
        aNode = list.pop()
        
        try:
            temp = hashTable.get(aNode['id']) #visited already
            continue
        except:
            pass
            
        hashTable.set(aNode.data[0], aNode) # mark as visited   

        msg = transition_state(previous.data[0], aNode.data[0])
        #print (msg)

        hp = abs(msg['event']['effect'])
        
        if aNode.data[0] == dst:
            finalNode = aNode
            found = True
            break
        aRoom = get_state(aNode.data[0])
        for neighbor in aRoom['neighbors']:
            try:
                hashTable.get(neighbor['id'])
            except:
                #aCost = cost(aRoom['location']['x'], aRoom['location']['y'], neighbor['location']['x'], neighbor['location']['y'])
                aNeighbor = Node([neighbor['id'], aNode.data[0], aNode.data[2] + hp, aRoom['location']['name']])
                list.push(aNeighbor)
        previous = aNode
        #print (list.length)
    if found == False:
        print ('Not found')
    else:
        path = ''
        current = aNode.data[0]
        current_name = aNode.data[3]
        while current != '':
            parent = hashTable.get(current).data[1]
            parent_name = hashTable.get(current).data[3]
            if  parent == '':
                break
            path = (parent_name + "(" + parent + ")" + " : " + current_name + "(" + current + ")") + '\n' + path
            current = parent
            current_name = parent_name;
        print (path)    
        print ('Total hp: ' + str(finalNode.data[2]))
        #print ('Total hp: ' + str(hp))

        
def Dijkstra(src, dst): 
    
    print ('Dijkstra Path:')
    
    list = List()
    hashTable = HashTable()
    finalNode = None
    found = False
    
    hp = 0
    empty_room = get_state(src)
    previous = Node([empty_room['id'], '', 0, empty_room['location']['name']])
    list.push(previous)
    
    while list.length > 0:
        #sort list      
        for i in range(0, list.length):
 
            key = list.memory[i]
            j = i - 1
            while j >= 0 and key.data[2] < list.memory[j].data[2] :
                    list.memory[j + 1].data[2] < list.memory[j].data[2]
                    j -= 1
            list.memory[j+1] = key
        
        #get the (best hp)
        aNode = list.pop()
        
        try:
            temp = hashTable.get(aNode['id'])#visited already
            continue
        except:
            pass
                
        hashTable.set(aNode.data[0], aNode) # mark as visited   

        msg = transition_state(previous.data[0], aNode.data[0])
        #print (msg)

        hp = abs(msg['event']['effect'])
        
        if aNode.data[0] == dst:
            finalNode = aNode
            found = True
            break
        aRoom = get_state(aNode.data[0])
        for neighbor in aRoom['neighbors']:
            
            try:
                aNodeInHash = hashTable.get(neighbor['id'])
                #choose better parent?
                #aCost = cost(aRoom['location']['x'], aRoom['location']['y'], neighbor['location']['x'], neighbor['location']['y'])
                
                #print (aNode.data[2] + aCost)
                #print (aNodeInHash.data[2])
                #print 'abc';
                #print 'abc';
            except:
                #aCost = cost(aRoom['location']['x'], aRoom['location']['y'], neighbor['location']['x'], neighbor['location']['y'])
                
                inList = False
                foundNode = None
                for i in range(0, list.length):
                    if list.memory[i].data[0] == neighbor['id']:
                        inList = True
                        foundNode = list.memory[i]
                        break
                        
                if inList == False:
                    aNeighbor = Node([neighbor['id'], aNode.data[0], aNode.data[2] + hp, aRoom['location']['name']])
                    list.push(aNeighbor)
                else:
                    if aNode.data[2] + hp > foundNode.data[2]:
                        foundNode.data[2] = aNode.data[2] + hp
                        foundNode.data[1] = aNode.data[0]
                
                
        previous = aNode
        #print (list.length)
    if found == False:
        print ('Not found')
    else:
        path = ''
        current = aNode.data[0]
        current_name = aNode.data[3]
        while current != '':
            parent = hashTable.get(current).data[1]
            parent_name = hashTable.get(current).data[3]
            if  parent == '':
                break
            path = (parent_name + "(" + parent + ")" + " : " + current_name + "(" + current + ")") + '\n' + path
            current = parent
            current_name = parent_name;
            print (parent_name + "(" + parent + ")" + " : " + current_name + "(" + current + ")")
        print (path)    
        print ('Total hp: ' + str(finalNode.data[2]))
        #print ('Total hp: ' + str(hp))
    
    pass
if __name__ == "__main__":
    # Your code starts here
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    #print(empty_room)
    #print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))
    
    src = '7f3dc077574c013d98b2de8f735058b4'
    dst = 'f1f131f647621a4be7c71292e79613f9'
    
    BFS(src, dst)
    
    Dijkstra(src, dst)
    
    

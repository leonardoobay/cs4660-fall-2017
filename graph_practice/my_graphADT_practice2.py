###################################################################
""" Chapter 14, page 634
14.2.5 Python Implementation
In this section, we provide an implementation of the Graph ADT. Our implementation
will support directed or undirected graphs, but for ease of explanation, we first
describe it in the context of an undirected graph. """
##################################################################





######################################################################
#------------------------- nested Vertex class -------------------------
#######################################################################
class Vertex:
 """Lightweight vertex structure for a graph."""
    slots = _element

  def init (self, x):
 
 """Do not call constructor directly. Use Graph s insert vertex(x)."""
    self.element = x

  def element(self):
 """Return element associated with this vertex."""
    return self.element

  def hash (self): # will allow vertex to be a map/set key
    return hash(id(self))
 
 
 #######################################################################
 #------------------------- nested Edge class -------------------------
 ####################################################################### 
class Edge:
"""Lightweight edge structure for a graph."""
  slots = _origin , _destination , _element

def init (self, u, v, x):
"""Do not call constructor directly. Use Graph s insert edge(u,v,x)."""
  self. origin = u
  self. destination = v
  self. element = x

def endpoints(self):
"""Return (u,v) tuple for vertices u and v.""
  return (self. origin, self. destination)

def opposite(self, v):
"""Return the vertex that is opposite v on this edge."""
  return self. destination if v is self. origin else self. origin

def element(self):
"""Return element associated with this edge."""
  return self. element

def hash (self): # will allow edge to be a map/set key
  return hash( (self. origin, self. destination) )



###############################################################################
##############################################################################
##############################################################################
1 class Graph:
2 ”””Representation of a simple graph using an adjacency map.”””
3
4 def init (self, directed=False):
5 ”””Create an empty graph (undirected, by default).
6
7 Graph is directed if optional paramter is set to True.
8 ”””
9 self. outgoing = { }
10 # only create second map for directed graph; use alias for undirected
11 self. incoming = { } if directed else self. outgoing
12
13 def is directed(self):
14 ”””Return True if this is a directed graph; False if undirected.
15
16 Property is based on the original declaration of the graph, not its contents.
17 ”””
18 return self. incoming is not self. outgoing # directed if maps are distinct
19
20 def vertex count(self):
21 ”””Return the number of vertices in the graph.”””
22 return len(self. outgoing)
23
24 def vertices(self):
25 ”””Return an iteration of all vertices of the graph.”””
26 return self. outgoing.keys( )
27
28 def edge count(self):
29 ”””Return the number of edges in the graph.”””
30 total = sum(len(self. outgoing[v]) for v in self. outgoing)
31 # for undirected graphs, make sure not to double-count edges
32 return total if self.is directed( ) else total // 2
33
34 def edges(self):
35 ”””Return a set of all edges of the graph.”””
36 result = set( ) # avoid double-reporting edges of undirected graph
37 for secondary map in self. outgoing.values():
38 result.update(secondary map.values()) # add edges to resulting set
39 return result
40 def get edge(self, u, v):
41 ”””Return the edge from u to v, or None if not adjacent.”””
42 return self. outgoing[u].get(v) # returns None if v not adjacent
43
44 def degree(self, v, outgoing=True):
45 ”””Return number of (outgoing) edges incident to vertex v in the graph.
46
47 If graph is directed, optional parameter used to count incoming edges.
48 ”””
49 adj = self. outgoing if outgoing else self. incoming
50 return len(adj[v])
51
52 def incident edges(self, v, outgoing=True):
53 ”””Return all (outgoing) edges incident to vertex v in the graph.
54
55 If graph is directed, optional parameter used to request incoming edges.
56 ”””
57 adj = self. outgoing if outgoing else self. incoming
58 for edge in adj[v].values( ):
59 yield edge
6061 def insert vertex(self, x=None):
62 ”””Insert and return a new Vertex with element x.”””
63 v = self.Vertex(x)
64 self. outgoing[v] = { }
65 if self.is directed( ):
66 self. incoming[v] = { } # need distinct map for incoming edges
67 return v
68
69 def insert edge(self, u, v, x=None):
70 ”””Insert and return a new Edge from u to v with auxiliary element x.”””
71 e = self.Edge(u, v, x)
72 self. outgoing[u][v] = e
73 self. incoming[v][u] = e

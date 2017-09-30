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
class Graph:
"""Representation of a simple graph using an adjacency map."""

def init (self, directed=False):
"""Create an empty graph (undirected, by default)

Graph is directed if optional paramter is set to True.
"""
self.outgoing = { }
# only create second map for directed graph; use alias for undirected
self.incoming = { } if directed else self. outgoing

def is directed(self):
"""Return True if this is a directed graph; False if undirected.

   Property is based on the original declaration of the graph, not its contents."""

  return self. incoming is not self. outgoing # directed if maps are distinct

def vertex count(self):
""" Return the number of vertices in the graph."""
   return len(self. outgoing)

def vertices(self):
   """ Return an iteration of all vertices of the graph."""
   return self. outgoing.keys( )

def edge count(self):
    """Return the number of edges in the graph."""
   total = sum(len(self. outgoing[v]) for v in self. outgoing)
# for undirected graphs, make sure not to double-count edges
return total if self.is directed( ) else total // 2

def edges(self):
"""Return a set of all edges of the graph."""
   result = set( ) # avoid double-reporting edges of undirected graph
   for secondary map in self.outgoing.values():
   result.update(secondary map.values()) # add edges to resulting set
   return result

def get edge(self, u, v):
   """Return the edge from u to v, or None if not adjacent."""
   return self. outgoing[u].get(v) # returns None if v not adjacent

def degree(self, v, outgoing=True):
   """Return number of (outgoing) edges incident to vertex v in the graph.

      If graph is directed, optional parameter used to count incoming edges."""
   adj = self. outgoing if outgoing else self. incoming
  return len(adj[v])

def incident edges(self, v, outgoing=True):
   """Return all (outgoing) edges incident to vertex v in the graph.

      If graph is directed, optional parameter used to request incoming edges.
   """
   adj = self. outgoing if outgoing else self. incoming
   for edge in adj[v].values( ):
   yield edge

def insert vertex(self, x=None):
"""Insert and return a new Vertex with element x."""
   v = self.Vertex(x)
   self. outgoing[v] = { }
   if self.is directed( ):
   self. incoming[v] = { } # need distinct map for incoming edges
   return v

def insert edge(self, u, v, x=None):
"""Insert and return a new Edge from u to v with auxiliary element x."""
   e = self.Edge(u, v, x)
  self. outgoing[u][v] = e
  self. incoming[v][u] = e

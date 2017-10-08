try:
  from graph.graph import Node, Edge
except:
  from graph import Node, Edge

# from graph import Node
# from graph import Edge

# not passing on python2

"""
utils package is for some quick utility methods

such as parsing
"""

class Tile(object):
    """Node represents basic unit of graph"""
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

    def __str__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)
    def __repr__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.symbol == other.symbol
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other_node):
        return self.__hash__() > other_node.__hash__()

    def __lt__(self, other_node):
        return self.__hash__() < other_node.__hash__()

    def __hash__(self):
        return hash(str(self.x) +"," + str(self.y) + self.symbol)



def parse_grid_file(graph, file_path):
    """
    ParseGridFile parses the grid file implementation from the file path line
    by line and construct the nodes & edges to be added to graph

    Returns graph object
    """
    # TODO: read the filepaht line by line to construct nodes & edges
    def check_symbol(cnode, symbol, x, y):
      if symbol != "##":    
        node = Node(Tile(int(x/2), y, tsymbol))
        edge = Edge(cnode, node, 1)
        graph.add_node(node)
        graph.add_edge(edge)


    f = open(file_path, 'r')
    lines = f.read().split('\n')[1:-2]
    lines = [l[1:-1] for l in lines]
    f.close()

    rows = len(lines)
    cols = len(lines[0])
    
    for row in range(rows):
        for col in range(0, cols, 2):
          symbol = lines[row][col:col+2]
          if symbol == "##" :
            continue
          tile = Tile(int(col/2), row, symbol)
          cur_node = Node(tile)
          graph.add_node(cur_node)

          # Look for left, right, top, bottom for edges
          if row - 1 >= 0:
            tsymbol = lines[row-1][col:col+2]
            check_symbol(cur_node, tsymbol, col, row-1)
          if row + 1 < rows:
            tsymbol = lines[row+1][col:col+2]
            check_symbol(cur_node, tsymbol, col, row+1)
          if col - 2 >= 0:
            tsymbol = lines[row][col-2:col]
            check_symbol(cur_node, tsymbol, col-2, row)
          if col + 2 < cols :
            tsymbol = lines[row][col+2:col+4]
            check_symbol(cur_node, tsymbol, col+2, row)
    
    # TODO: for each node/edge above, add it to graph

    return graph

def convert_edge_to_grid_actions(edges):
    """
    Convert a list of edges to a string of actions in the grid base tile

    e.g. Edge(Node(Tile(1, 2), Tile(2, 2), 1)) => "S"
    """
    path = ""
    
    for edge in edges:
      
      tile1 = edge.from_node.data
      tile2 = edge.to_node.data

      if tile2.y > tile1.y:
        path += "S"
      elif tile2.x > tile1.x:
        path += "E"
      elif tile2.y < tile1.y:
        path += "N"
      elif tile2.x < tile1.x:
        path += "W"
    return path

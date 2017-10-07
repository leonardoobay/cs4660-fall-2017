from collections import defaultdict
from graph.utils import convert_edge_to_grid_actions
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]


"""
Searches module defines all different search algorithms
"""

def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """

    visited = set()
    queue = [(initial_node, [], visited)]
    while queue:
        (vertex, path, visited) = queue.pop(0)
        visited.add(vertex)
        for next in graph.neighbors(vertex):
            if next in visited:
                continue
            if next == dest_node:
                final_path = path + [graph.distance(vertex, next)]
                return final_path
            else:
                queue.append((next, path + [graph.distance(vertex, next)], visited))


def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """

    visited = set()
    stack = [(initial_node, [], visited)]
    while stack:
        (vertex, path, visited) = stack.pop()
        if vertex == dest_node:
            final_path = path
            return final_path
        s = [x[0] for x in stack]        
        print("Popping from stack", vertex.data, s)
        visited.add(vertex)
        for next in graph.neighbors(vertex)[::-1]:
            if next in visited:
                continue
            stack.append((next, path + [graph.distance(vertex, next)], visited))
            s = [x[0] for x in stack]        
            print("Pushing to stack", next.data, s)
    
    

def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """

    queue = [initial_node]
    distances = {}
    distances =  defaultdict(lambda:9999999999999, distances)
    distances[initial_node] = 0
    visited = set()
    path = {}
    path[initial_node] = None

    while queue:
        min_dist = 9999999999999
        min_node = None
        # Pick the node with lowest distance
        for q in queue:
        # for node, dist in distances.items():
            if distances[q] < min_dist:
                min_dist = distances[q]
                min_node = q 
        visited.add(min_node)
        del(queue[queue.index(min_node)])
        
        for v in graph.neighbors(min_node):
            if min_dist + graph.distance(min_node, v).weight < distances[v]:
                distances[v] = min_dist + graph.distance(min_node, v).weight
                path[v] = min_node
            queue.append(v)
    n = dest_node
    path_list = [n]
    while path[n]:
        path_list.append(path[n])
        n = path[n]
    path_list = path_list[::-1]
    final_path = []
    for v, w in zip(path_list[:-1], path_list[1:]):
        final_path.append(graph.distance(v, w))

    return final_path

def a_star_search(graph, initial_node, dest_node):
    print(graph)
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """


    def heuristic(a, b):
        x1, y1 = a.data.x, a.data.y
        x2, y2 = b.data.x, b.data.y
        return abs(x1 - x2) + abs(y1 - y2)
    
    frontier = PriorityQueue()
    frontier.put(initial_node, 0)
    came_from = {}
    cost_so_far = {}
    came_from[initial_node] = None
    cost_so_far[initial_node] = 0
    
    while not frontier.empty():
        current = frontier.get()
        if current == dest_node:
            break
    
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.distance(current, next).weight
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(dest_node, next)
                frontier.put(next, priority)
                came_from[next] = current

    n = dest_node
    path_list = [n]
    while came_from[n]:
        path_list.append(came_from[n])
        n = came_from[n]
    path_list = path_list[::-1]
    final_path = []
    for v, w in zip(path_list[:-1], path_list[1:]):
        final_path.append(graph.distance(v, w))
    return final_path

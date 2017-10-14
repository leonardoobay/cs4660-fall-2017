def find_path(graph, start, end, path=[]): # four parameters, one of which is a list.
        path = path + [start]              # pass the start parameter to the list
        if start == end:                   
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None
        
        
        
        ##################################
        Sample run
         >>> find_path(graph, 'A', 'D')
    ['A', 'B', 'C', 'D']
    >>> 

#################################
# Interesting way of reading files
# Source: https://www.ics.uci.edu/~pattis/common/modules/courselib/graph.py
#
#
#
#
###############################



def read(self,file,conv=(lambda x : x),sep=' '):
        """
        Read a graph from a text file; assume sep is separating the nodes and edge values
        conv converts the string value of an edge into the appropriate type of value
        Graphs written by write should be readable by read
        """
        nodes_only = True
        for line in file:
            if line == 'NODESABOVEEDGESBELOW\n':
                nodes_only = False
                continue
            if nodes_only:
                self.add_node(line.strip())
            else:
                e = line.strip().split(sep)
                self.add_edge((e[0],e[1]),conv(e[2]))

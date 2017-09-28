
[https://github.com/csula-students/cs4660-fall-2017-cs4660csula/blob/master/traversal_practice/images/dungeons_walkthrough.png|alt=code]

[[https://github.com/username/repository/blob/master/img/octocat.png|alt=octocat]]



def walk(G, s, S=set()):                        # Walk the graph from node s
    P, Q = dict(), set()                        # Predecessors + "to do" queue
    P[s] = None                                 # s has no predecessor
    Q.add(s)                                    # We plan on starting with s
    while Q:                                    # Still nodes to visit
          u = Q.pop()                           # Pick one, arbitrarily
    for v in G[u].difference(P, S):             # New nodes?
        Q.add(v)                                # We plan to visit them!
    P[v] = u                                    # Remember where we came from
    return P                                    # The traversal tree

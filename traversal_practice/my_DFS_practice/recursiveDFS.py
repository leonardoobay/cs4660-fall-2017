def rec_dfs(G, s, S=None):                                 # We have three parameters
  if S is None: S = set()                                  # Initialize the history
  S.add(s)                                                 # We've visited s
  for u in G[s]:                                           # Explore neighbors
  if u in S: continue                                      # Already visited: Skip
  rec_dfs(G, u, S)                                         # New: Explore recursively
  
  
  
  
  
  """
  page 110 chapter 5
  
  Book: Python Algorithms Mastering Basic Algorithms in the Python Language
  
  """

class node:
  
def __init__(self, name, population=0):
    self._name = name
    self._pop = population

def getName(self):
    return self._name

def getPopulation(self):
    return self._pop

class edge:

    def __init__(self, name1, name2, weight=0):
       self._city1 = name1
       self._city2 = name2
       self._distance = weight

def getName1(self):
    return self._city1

def getName2(self):
    return self._city2

def getNames(self):
    return (self._city1, self._city2)

def getWeight(self):
    return self._distance

  
  
  
  """ Adding city code for the graph
  The following is how we might set up our node list and edge list for the 
city example. We’ll create our five cities, each with some population, and 
add  those  to  the  city  list.  For  example,  we  create  a  node  for  Rivertown  
with a population of 100 and append it to the cities list.
  
  """
  
  
cities = []
roads = []
city = node('Rivertown', 1000)
cities.append(city)
city = node('Brookside', 1500)
cities.append(city)
city = node('Hillsview', 500)
cities.append(city)
city = node('Forrest City', 800)
cities.append(city)
city = node('Lakeside', 1100)
cities.append(city)
road = edge('Rivertown', 'Brookside', 100)
roads.append(road)
road = edge('Rivertown', 'Hillsview', 50)
roads.append(road)
road = edge('Hillsview', 'Brookside', 130)
roads.append(road)
road = edge('Hillsview', 'Forrest City', 40)
roads.append(road)
road = edge('Forrest City', 'Lakeside', 80)
roads.append(road)

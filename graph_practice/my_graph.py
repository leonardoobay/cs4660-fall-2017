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

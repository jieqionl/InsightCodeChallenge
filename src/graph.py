# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 11:52:05 2016

@author: Jieqiong Liu
"""

class Vertex:
    def __init__(self, personName):
        self.name = personName
        self.edges = {}
        
    def __str__(self):
        return str(self.name) + ' edgedTo: ' \
            + str([x.name for x in self.edges])

    # record num of payments between 2 people        
    def addNeighbor(self, nbr):
        if nbr in self.edges:
            self.edges[nbr] += 1
        else:
            self.edges[nbr] = 1
    
    def delNeighbor(self, nbr):
        if self.edges[nbr] > 1:
            self.edges[nbr] -= 1
        else:
            del self.edges[nbr]
    
    def getDegree(self):
        return len(self.edges.keys())
        
    def getName(self):
        return self.name

        
class Graph:
    def __init__(self):
        self.vertexDict = {}
        self.numVertex = 0
    
    # in order to use if...in...
    def __contains__(self, personName):
        return personName in self.vertexDict
    
    # in order to use for...in...    
    def __iter__(self):
        return iter(self.vertexDict.values())
        
    def addVertex(self, personName):
        self.numVertex += 1
        newVertex = Vertex(personName)
        self.vertexDict[personName] = newVertex
        return newVertex
        
    def delVetex(self, personName):
        if personName in self.vertexDict:
            if self.vertexDict[personName].getDegree() == 0:
                del self.vertexDict[personName]
    
    def addEdge(self, u, v):
        if u not in self.vertexDict:
            self.addVertex(u)
        if v not in self.vertexDict:
            self.addVertex(v)
        self.vertexDict[u].addNeighbor(self.vertexDict[v])
        self.vertexDict[v].addNeighbor(self.vertexDict[u])
        
    def delEdge(self, u, v):
        if u in self.vertexDict and v in self.vertexDict:
            self.vertexDict[u].delNeighbor(self.vertexDict[v])
            self.vertexDict[v].delNeighbor(self.vertexDict[u])
            
    def getVertex(self, personName):
        if personName in self.vertexDict:
            return self.vertexDict[personName]
        else:
            return None
            
    def getVertexKeys(self):
        return self.vertexDict.keys()
        
    def findMedianDegree(self):
        alldegree = []
        for node in self.vertexDict.values():
            if node.getDegree() > 0:
                alldegree.append(node.getDegree())
        alldegree.sort()
        n = len(alldegree)
        if n % 2 != 0:        
            return alldegree[n//2]
        else:
            return (alldegree[n//2-1] + alldegree[n//2])/2
            
def unitTest():
    g = Graph()
    g.addVertex('JG')
    g.addVertex('JK')
    g.addVertex('YM')
    g.addVertex('MB')
    g.addEdge('JG', 'JK')
    g.addEdge('MB', 'JK')
    g.addEdge('YM', 'MB')
    g.addEdge('JK', 'YM')
    assert g.findMedianDegree() == 2.0
    g.delEdge('YM', 'JK')
    assert g.findMedianDegree() == 1.5
    
if __name__ == "__main__":
    unitTest()
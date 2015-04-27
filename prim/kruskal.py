import sys
import random
sys.path.append('../dataStructures/graphs')
from graph import *

def notEmpty(myList):
    if myList:
        return True
    else:
        return False

'''
* Important Note: Kruskal's algorithm is for undirected graphs. I assume that every edge is bidirectional in this implementation. You could have an adjacency list with both edges: 
    a b 1 
    b a 1 
    but, this algorithm will work with a single edge:
    a b 1
* Algorithm (Kruskal's algorithm is more elegant than Prim's, in my humble opinon):
    1. Get a list of edges
    2. Add an edge that does not create a cycle (another way to think of it: an edge that visits a new vertex, this is how I implemented it)
    3. Repeat 2 until there no edges that do not form a cycle (aka no unvisited vertices) 
* Running time:
    This implementation runs in O(VE)
    * O(E) to iterate over all edges
    * O(V) to check for cycles
        
'''
def kruskal(G):
    edges = []
    for edge in G.adjacencyList:
        edges.append(edge)
    unvisited = G.getListVertexNames()
    MST = []

    while notEmpty(unvisited):
        newEdges = []
        for edge in edges: 
            v1 = edge['startVertex']
            v2 = edge['endVertex']
            if (v1 in unvisited) or (v2 in unvisited):
                newEdges.append(edge)

        minEdge = min(newEdges, key = lambda e: e['weight'])

        v1 = minEdge['startVertex']
        v2 = minEdge['endVertex']
        if v1 in unvisited:
            unvisited.remove(v1)
        if v2 in unvisited:
            unvisited.remove(v2)
        edges.remove(edge)
        MST.append(minEdge)

    return MST

fname = raw_input("Enter graph filename(defaults to graphData.data)': ")
if fname:
    G = Graph(fname)
else:
    G = Graph("graphData.data")
mstEdges = kruskal(G)
for edge in mstEdges:
    print edge['startVertex'], edge['endVertex'], edge['weight']

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
* Important Note: Prim's algorithm is for undirected graphs. Using the graph implementation in datastructures/graphs, all edges must be listed bidirectionally, example: 
    a b 1 
    b a 1 
    both of the above must be listed
* Algorithm:
    1. Make a list of all unvisited and visited vertices
    2. Start at a random vertex, add it to visited, remove from unvisited
    3. Iterate over all edges, and keep track of those that extend the MST, aka extend the visited set. I call these the 'frontier' 
    4. Add the minimum edge in the frontier to the MST (in graph jargon, this is the minimum cut), and update visited/unvisited 
    5. Repeat 3 and 4 until all vertices are visited
* Running time:
    This implementation runs in O(VE), it could be sped up using a minimum heap 
'''
def prim(G):
    visited = []
    unvisited = G.getListVertexNames()
    start = unvisited[random.randint(0, len(unvisited)-1)]
    visited.append(start)
    unvisited.remove(start)
    MST = []

    while notEmpty(unvisited):
        frontier = []
        for edge in G.adjacencyList:
            if((edge['startVertex'] in visited) and (edge['endVertex'] in unvisited)):
                frontier.append(edge)

        firstEdge = frontier[0]
        minEdge = firstEdge 
        minGreedyScore = firstEdge['weight']
        for edge in frontier:
            greedyScore = edge['weight']
            if(greedyScore < minGreedyScore):
                minEdge = edge
                minGreedyScore = greedyScore
        
        visited.append(minEdge['endVertex'])
        unvisited.remove(minEdge['endVertex'])
        MST.append(minEdge)

    return MST

fname = raw_input("Enter graph filename(defaults to graphData.data)': ")
if fname:
    G = Graph(fname)
else:
    G = Graph("graphData.data")
mstEdges = prim(G)
for edge in mstEdges:
    print edge['startVertex'], edge['endVertex'], edge['weight']

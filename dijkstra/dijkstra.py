import sys
sys.path.append('../dataStructures/graphs')
from graph import *

def notEmpty(myList):
    if myList:
        return True
    else:
        return False

def dijkstra(G, start, end):
    visited = []
    bigNumber = 10000000
    unvisited = G.getListVertexNames()
    G.getListVertexNames()
    distances = {}
    for vertex in unvisited:
        distances[vertex] = bigNumber 
    distances[start] = 0 
    visited.append(start)
    unvisited.remove(start)

    while notEmpty(unvisited):
        frontier = []
        for edge in G.adjacencyList:
            if((edge['startVertex'] in visited) and (edge['endVertex'] in unvisited)): 
                frontier.append(edge)

        minEdge = frontier[0]
        firstEdge = frontier[0]
        minGreedyScore = firstEdge['weight'] + distances[firstEdge['startVertex']]
        for edge in frontier:
            greedyScore = edge['weight'] + distances[edge['startVertex']]
            if(greedyScore < minGreedyScore):
                minEdge = edge
                minGreedyScore = greedyScore
        
        visited.append(minEdge['endVertex'])
        unvisited.remove(minEdge['endVertex'])
        distances[minEdge['endVertex']] = minEdge['weight'] + distances[minEdge['startVertex']]
    return distances[end]

fname = raw_input("Enter graph filename(defaults to graphData.data)': ")
start = raw_input("Enter graph start vertex: ")
end = raw_input("Enter graph end vertex: ")
if fname:
    G = Graph(fname)
else:
    G = Graph("graphData.data")
print dijkstra(G, start, end)

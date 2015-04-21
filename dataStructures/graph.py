import copy

class Vertex:
    name = ""
    edges = []
    def __init__(self, name):
        self.name = name

    def addEdge(self, edge):
        self.edges.append(edge)

    def isConnectedTo(self, vertexName):
        for edge in self.edges:
            if(edge[0]==vertexName):
                return True
        return False

    def getEdges(self, vertexName):
        for edge in self.edges:
            if(edge[0]==vertexName):
                return True
        return False

class Graph:
    adjacencyList = []
    vertices = []
    def __init__(self, fname):
        lines = [line.strip() for line in open(fname)]
        for line in lines:
            edgeData = line.split(' ')
            startVertex = Vertex(edgeData[0])
            endVertex = Vertex(edgeData[1])
            weight = int(edgeData[2])

            startVertex.addEdge((endVertex.name, weight))
            adjacencyListElement = {'startVertex': startVertex.name, 'endVertex': endVertex.name, 'weight': weight}
            self.adjacencyList.append(adjacencyListElement)
            if startVertex.name not in self.vertices:
                self.vertices.append(startVertex.name)
            if endVertex.name not in self.vertices:
                self.vertices.append(endVertex.name)

    def printAdjacencyList(self):
        for edge in self.adjacencyList:
            print edge['startVertex'], "---->", edge['endVertex'], edge['weight']

    def getListVertexNames(self):
        return copy.deepcopy(self.vertices)


    def getVertex(self, vertexName):
        if vertexName not in self.vertices:
            return None
        else:
            vertex = Vertex(vertexName)
            for edge in self.adjacencyList:
                if(edge['startVertex']==vertexName):
                    vertex.addEdge((edge['endVertex'], edge['weight']))
            return vertex

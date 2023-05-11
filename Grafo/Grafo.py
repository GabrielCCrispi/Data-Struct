class Vertex:
    
    def __init__(self,data):

        self.data = data

class Graph:
    
    def __init__(self, directed = False):
        
        self.verticesList = []
        self.adjList = []
        
        self.directed = directed
    
    def addVertex(self, data):
        
        vertice = Vertex(data)
        
        self.verticesList.append( vertice )
        
        self.adjList.append( [] )
        
# testa o grafo
grafo1 = Graph( directed = False )
grafo1.addVertex('A')
grafo1.addVertex('B')
grafo1.addVertex('C')
grafo1.addVertex('D')
grafo1.addVertex('E')
grafo1.addVertex('F')
grafo1.addVertex('G')
grafo1.addVertex('H')

print(grafo1.verticesList)
print(grafo1.adjList)
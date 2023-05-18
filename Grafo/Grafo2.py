class Vertex:
    """
    Noh para uma arvore AVL
    """
    
    def __init__(self, data):
        
        self.data = data
        
class Graph:
    """
    Arvore AVL - implementacao dinamica
    """

    def __init__(self, directed=False):
        
        # a lista de vertices inicia vazia
        self.verticesList = []
        self.adjList = []
        self.directed = directed
 
        
    def addVertex(self, data, directed=False):
        """
        Adiciona um vertice no grafo
        """

        # crim um novo vertice
        tempVertice = Vertex(data)
        
        # adiciona o novo vertice na lista de vertices
        self.verticesList.append(tempVertice)
        
        # adiciona uma lista de adjacencias vazia para o novo vertice
        vertexAdj = []
        self.adjList.append( vertexAdj )
        
    def addEdge(self,origin,destination):
        """
        Adiciona uma aresta entre o vertice que contem o 
        valor origin e o vertice que contem o valor destination
        """
        
        idxOrig = -1
        idxDest = -1
        for idx, vertex in enumerate(self.verticesList):
            if vertex.data == origin:
                idxOrig = idx
            if vertex.data == destination:
                idxDest = idx 
           
        # se origin or destination forem invalidos, encerra o metodo
        # sem fazer nenhuma alteracao
        if idxOrig==-1 or idxDest==-1:
            return
        
        # adiciona a vertice de destino como adjacente ao vertice de origem
        self.adjList[idxOrig].append( idxDest )
        
        # se o grafo nao e orientado, adiciona o vertice de origem como adjacente ao vertice de destino
        if self.directed==False: 
            self.adjList[idxDest].append( idxOrig )
            
    def exploreVertex(self, firstVertex = 0, cor = None):

        strBFS = ''

        branco = 0
        cinza = 1
        preto = 2

        if cor is None:
            cor = [branco] * len(self.verticesList)

        cor[firstVertex] = cinza

        strBFS += str(self.verticesList[firstVertex].data)

        # inicia a fila vazia
        fila = []     

        # adiciona o vertice
        fila.append(firstVertex)
        
        
        while len(fila) > 0:
            
            idxVertex = fila[0]

            for idxAdj in self.adjList[idxVertex]:
                
                if cor[idxAdj] == branco:
                
                 cor[idxAdj] = cinza

                fila.append(idxAdj)
                
                #imprime o vertice visitado
                strBFS += ' ' + str(self.verticesList[idxAdj].data)
                
            cor[idxVertex] = preto
            
            #elimina o vertice visitado
            fila.pop(0)
        return strBFS, cor
                        
    def __str__(self):
        
        info = '\nLista de adjacencia:\n'+20*'='+'\n'
        for idx, vertex in enumerate(self.verticesList):
            
            info += str(vertex.data) + ': ['
            for idxAdj in self.adjList[idx]:
                data = self.verticesList[idxAdj].data
                info += str(data) + ' '
            
            info += ']\n'
            
        info += 20*'='+'\n'
            
        
        return info
            

if __name__ == "__main__":

    # cria o primeiro grafo
    grafo = Graph(directed=False)
    grafo.addVertex('A')
    grafo.addVertex('B')
    grafo.addVertex('C')
    grafo.addVertex('D')
    grafo.addVertex('E')
    grafo.addVertex('F') 
    grafo.addVertex('G')
    grafo.addVertex('H')

    grafo.addEdge('B','F')
    grafo.addEdge('B','A')    
    grafo.addEdge('A','E')
    grafo.addEdge('F','C')
    grafo.addEdge('F','G')
    grafo.addEdge('C','G')
    grafo.addEdge('C','D')
    grafo.addEdge('D','H')
    grafo.addEdge('h','G')
    
    print(grafo)
    strBFS += str(self.verticesList[firstVertex].data)
    print(strBFS)
     
    # cria o segundo grafo
    grafo = Graph(directed=True)
    grafo.addVertex('A')
    grafo.addVertex('B')
    grafo.addVertex('C')
    grafo.addVertex('D')
    grafo.addVertex('E')
    grafo.addVertex('F') 

    grafo.addEdge('A','C')    
    grafo.addEdge('A','B')
    grafo.addEdge('B','C')
    grafo.addEdge('C','F')
    grafo.addEdge('D','E')
    grafo.addEdge('E','C')
    
    print()
    print(grafo)
    print( 'BFS (largura): ',grafo.breadthFirstSearch() )
    print( 'DFS (profundidade): ',grafo.depthFirstSearch() )
    
    
    
class GraphMatrix:
    
    def __init__(self, directed = False):
        
        self.directed = directed
        self.verticesList = []
        self.adjMat = []
        
    def addVertex(self, valor):
        
        vertNovo = Vertex(valor)
        
        for i, vert in enumerate(self.verticesList):
            self.adjMat[i].append(0)
            
        self.verticesList.append(vertNovo)
        
        listaZeros = [0] * len(self.verticesList)
        self.adjMat.append( listaZeros )
        
    def __str__(self):
        
        strGrafo = '  '
        for i, vert in enumerate(self.verticesList):
            strGrafo += "  " + str(vert.data)
            
        for lin, vert in enumerate( self.verticesList ):
            
            strGrafo += '\n' + str(vert.data) + ': '
            
            for col, vertCol in enumerate( self.verticesList ):
                strGrafo += ' ' + str(self.adjMat[lin][col] ) + " "
            
            
        return strGrafo
        
    
grafo1 = GraphMatrix(directed=False)
grafo1.addVertex(1)
grafo1.addVertex(2)
grafo1.addVertex(3)
grafo1.addVertex(4)
grafo1.addVertex(5)
grafo1.addVertex(6)

print(grafo1)
        
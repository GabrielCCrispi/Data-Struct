class Node:
    
    def __init__(self, data,
                 left = None,
                 right = None):

        self.data = data
        self.left = left
        self.right = right
    
class Tree:
    
    def __init__(self):
        
        self.root = None
    
    def insert(self,valor, nohAtual = None):
        
        if self.root is None:
            self.root = Node(valor)
        
        else:
            
            if nohAtual is not None:
                nohAtual = Node(valor)
            
            if valor < nohAtual.data:
                self.insert( nohAtual.left)

            else: 
                self.insert( valor, nohAtual.right )

def preOrdem(raiz, strArvore = ""):
    
    if raiz is None:
        return strArvore
    
    else:
        strArvore += " " + str(raiz.data)
        
        strArvore += "("
    
        if raiz.left is not None:
            strArvore +=  preOrdem( raiz.left )
        
        if raiz.right is not None:
            strArvore += preOrdem( raiz.right )
        
        strArvore += ")"
        
        return strArvore
    
noh17 = Node(17)
noh6 = Node(6)
noh35 = Node(35)
noh4 = Node(4)
noh14 = Node(14)
noh23 = Node(23)
noh48 = Node(48)

noh17.left = noh6
noh17.right = noh35

noh6.left = noh4
noh6.right = noh14

noh35.left =noh23
noh35.right = noh48

print( preOrdem(noh17) )

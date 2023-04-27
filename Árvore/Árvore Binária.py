class Node:
    
    def __init__(self, data,
                 left = None,
                 right = None):

        self.data = data
        self.left = left
        self.right = right


def preOrdem(raiz, strArvore = ""):
    
    if raiz is None:
        return strArvore
    
    else:
        strArvore += " " + raiz.data
    
        if raiz.left is not None:
            strArvore +=  preOrdem( raiz.left )
        
        if raiz.right is not None:
            strArvore += preOrdem( raiz.right )
        
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

print( noh17.left.right.data )

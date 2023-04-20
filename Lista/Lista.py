class Node:
    
    def __init__(self, data,
                 next = None,
                 prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Lista:
    
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.size = 0
    
    def insertHead(self, valor):
        
        novoNoh = Node(valor)
        
        if self.size == 0:
            self.head = novoNoh
            self.tail = novoNoh
        else:
            novoNoh.next = self.head
            self.head.prev = novoNoh
            
        self.size += 1
        
    def insertTail(self, valor):
        
        novoNoh = Node(valor)
        if self.size == 0:
            self.head = novoNoh
            self.tail = novoNoh
        else:
            novoNoh.prev = self.tail
            self.tail.next = novoNoh
            self.tail = novoNoh
        self.size += 1
    
    def insert(self, valor, pos):
        if pos == 0:
            self.insertHead(valor)
        elif pos == self.size:
            self.insertTail(valor)
        elif pos > self.size:
            print("Posição invalida")
            return        
        else:
            novoNoh = Node(valor)
            
            nohAux = self.head
            i = 0
            while i < pos:
                nohAux = nohAux.next
                i += 1
                        
            novoNoh.next = nohAux
            novoNoh.prev = nohAux.prev
            novoNoh.prev.next = novoNoh
            #nohAux.prev.next = novoNoh
            nohAux.prev = novoNoh
            #novoNoh.next.prev = novoNoh
            
            
    def __str__(self):
        
        strLista = "["
        
        nohAux = self.head
        while nohAux is not None:
            
         strLista += " " + str(nohAux.data)
            
         nohAux = nohAux.next
            
        strLista += "]"
        
        return strLista
        
#criar uma lista
lista1= Lista()
lista1.insert(8, 0)
lista1.insert(15, 1)
lista1.insert(7, 1)
lista1.insert(9, 2)
lista1.insert(11, 2)
print(lista1)


noh1 = Node(10)
noh2 = Node(15)
noh3 = Node(20)
noh4 = Node(25)

noh1.next = noh2
noh2.prev = noh1
noh2.next = noh3
noh3.prev = noh2
noh3.next = noh4
noh4.prev = noh3

#print( noh4.prev.prev.prev.data )
#print( noh1.next.next.next.data )

head = noh1 # primeiro
tail = noh4 # ultimo
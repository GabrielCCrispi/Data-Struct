class Deque:
    """
    Deque estatico circular
    """
        
    def __init__(self, capacity):

        self.capacity = capacity

        # inicializa a fila com o tamanho desejado
        self.queue = [None] * capacity
        
        # inicializa as posicoes do primeiro e ultimo 
        # elemento com -1
        self.front = -1
        self.rear = -1
        
        # no inicio, o tamanho da fila eh 0
        self.size = 0

    def enqueueRear(self, data):
        """
        Adiciona um elemento no final da fila
        """
        
        if self.size >= self.capacity:
            print("Estouro de fila")
            return
        
        else:
            
            # se for a primeira insercao na fila, precisa mudar os valores
            # das variaveis front e rear para 0
            if self.front==-1:
                self.front = 0
                self.rear = 0
            
            # se ultimo elemento da fila estiver no ultimo indice,
            # o novo elemento deve ser adicionado no indice 0.
            # Poderiamos evitar esse if se calculassemos o indice baseado
            # no resto da divisao de rear/capacity. Exemplo: se capacity
            # igual a 10 e rear igual a 9, (9+1)%10, daria 0. Se rear fosse
            # menor que 9, o (rear+1)%10 daria o proprio rear.
            elif self.rear==self.capacity-1:
                self.rear = 0
                
            else:
                self.rear = self.rear + 1
                
            # adiciona o elemento no final da fila
            self.queue[self.rear] = data
            
            # aumenta o tamanho
            self.size += 1
            

    def enqueueFront(self, data):
        """
        Adiciona um elemento no final da fila
        """
        
        if self.size >= self.capacity:
            print("Estouro de fila")
            return
        
        else:
            
            # se for a primeira insercao na fila, precisa mudar os valores
            # das variaveis front e rear para 0
            if self.front==-1:
                self.front = 0
                self.rear = 0
            
            # se primeiro elemento da fila estiver no indice 0,
            # o novo elemento deve ser adicionado na ultima posicao do vetor.
            elif self.front==0:
                self.front = self.capacity-1
                
            else:
                self.front = self.front - 1
                
            # adiciona o elemento
            self.queue[self.front] = data
            
            # aumenta o tamanho
            self.size += 1
            
            
    def dequeueFront(self):
        """
        Retorna e remove o elemento no inicio da fila
        """
        
        if self.size == 0:
            print("Fila vazia")
            return None
        
        else:
    
            # retorna o primeiro elemento
            temp = self.queue[self.front]
            
            # se o tamanho for 1, quando remover, os indices 
            # front e rear devem virar -1
            if self.size == 1:
                self.front = -1
                self.rear = -1
                
            # se primeiro elemento da fila estiver no ultimo indice,
            # o novo primeiro elemento sera o que esta no indice 0
            elif self.front == self.capacity-1:
                    self.front = 0
                    
            else:
                    self.front = self.front + 1
            
            # diminui o tamanho
            self.size -= 1

        return temp
    
    def dequeueRear(self):
        """
        Retorna e remove o elemento no final da fila
        """
        
        if self.size == 0:
            print("Fila vazia")
            return None
        
        else:
    
            # retorna o ultimo elemento
            temp = self.queue[self.rear]
            
            # se o tamanho for 1, quando remover, os indices 
            # front e rear devem virar -1
            if self.size == 1:
                self.front = -1
                self.rear = -1
                
            # se ultimo elemento da fila estiver na posicao 0,
            # o novo ultimo elemento sera o que esta no indice capacidade-1
            elif self.rear == 0:
                self.rear = self.capacity - 1
  
            else:
                self.rear = self.rear - 1 
            
            # diminui o tamanho
            self.size -= 1

        return temp
    
    def getSize(self):
        """
        Retorna a quantidade de elementos da fila
        """
        return self.size

    def isEmpty(self):
        """
        Retorna True se a fila esta vazia
        """
        return self.size == 0

    def isFull(self):
        """
        Retorna True se a fila esta cheia
        """
        return self.size == self.capacity

    def getFront(self):
        """
        Retorna o primeiro elemento da lista sem remover
        """
        
        if self.isEmpty():
            print("fila vazia")
            return None

        return self.queue[self.front]
    
    def clear(self):
        """
        Limpa a fila. Como o espaco para a fila ja esta 
        reservado, nao precisa efetivamente remover os valores.
        Basta alterar os indices e o valor size.
        """
        self.front = -1
        self.rear = -1
        self.size = 0
        


    def __str__(self):
        """
        Retorna uma string com as informacoes da fila
        quando o objeto e chamado dentro de um print() 
        ou dentro de um str(). 
        """
        
        # cria uma nova fila auxiliar
        auxfila = Deque(self.capacity)
        
        # retira os elementos da fila antiga e preenche a auxiliar
        for i in range( self.size ):
            auxfila.enqueueRear( self.dequeueFront() )
            
        # cria uma string com os elementos da fila auxiliar e
        # enquanto isso, preenche novamente a fila original
        strfila = '['
        for i in range( auxfila.size ):
            
            front = auxfila.dequeueFront()
            
            # preenche a fila original
            self.enqueueRear(front)
            
            # guarda o front em uma string
            strfila += ' ' + str(front)
            
        strfila += ' ]'
        
        return strfila
        
            
            
            
if __name__ == "__main__":
    

    deque1 = Deque(capacity=4)
    deque1.enqueueFront(5)
    deque1.enqueueFront(9)
    deque1.enqueueRear(3)
    deque1.enqueueRear(4)
    print('\n', deque1)  
    
    deque2 = Deque(capacity=4)
    deque2.enqueueFront(3)
    deque2.enqueueFront(4)
    deque2.enqueueRear(5)
    deque2.enqueueRear(9)
    print('\n', deque2)  
    
    deque3 = Deque(capacity=4)
    deque3.enqueueFront(5)
    deque3.enqueueFront(9)
    deque3.enqueueRear(1)
    deque3.enqueueRear(4)
    print('\n', deque3)           


    



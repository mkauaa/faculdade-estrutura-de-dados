class Nodo:
    def __init__(self, dado = 0, nodo_anterior = None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return f'{self.dado} -> {self.anterior}'

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def vazia(self):
        if self.topo == None:
            return True
        else:
            return False

    def insere(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo
        self.tamanho += 1

    def remove(self):
        if self.vazia():
            print('É impossível remover valores de uma pilha vazia.')
        
        else:
            removido = self.topo.dado
            self.topo = self.topo.anterior
            self.tamanho -= 1
            return removido
          
    def compara(self, pilha2):
      if self.tamanho != pilha2.tamanho:
        return False
      
      else:
        no_atual1 = self.topo
        no_atual2 = pilha2.topo
        
        while (no_atual1) != None:
          if (no_atual1.dado != no_atual2.dado):
            return False
          
          no_atual1 = no_atual1.anterior
          no_atual2 = no_atual2.anterior
          
        return True

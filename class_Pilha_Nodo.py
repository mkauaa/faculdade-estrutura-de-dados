class Nodo:
    def __init__(self, dado = 0, nodo_anterior = None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)

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
            print(f'O elemento {self.topo} foi removido.')
            self.topo = self.topo.anterior
            self.tamanho -= 1
            

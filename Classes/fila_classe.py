class NodoFila: 
  def __init__(self, dado = 0, proximo_nodo = None):
    self.dado = dado
    self.proximo = proximo_nodo
    
  def __repr__(self):
      return f'{self.dado} -> {self.proximo}'
    
class Fila:
  def __init__(self):
      self.cabeca = None
      self.cauda = None
      self.tamanho = 0
      
  def __repr__(self):
      return "[" + str(self.cabeca) + "]"
    
  def vazia(self):
    if self.cabeca == None:
      return True
    
    else:
      return False
    
  def insere(self, novo_dado):
    novo_nodo = NodoFila(novo_dado)
    
    if self.vazia():
      self.cabeca = novo_nodo
      self.cauda = novo_nodo
      
    else:
      self.cauda.proximo = novo_nodo
      self.cauda = novo_nodo

    self.tamanho += 1
      
  def remove(self):
    removido = self.cabeca.dado
    
    self.cabeca = self.cabeca.proximo
    if self.cabeca == None:
      self.cauda = None
      
    return removido

  def igual(self, f2):
    if self.tamanho != f2.tamanho:
        if self.tamanho > f2.tamanho:
            return ('F1 > F2')
        if self.tamanho < f2.tamanho:
            return ('F1 < F2')
      
    else:
        atual1 = self.cabeca
        atual2 = f2.cabeca
        
        while atual1 != None:
            if atual1.dado != atual2.dado:
                return False
            
            atual1 = atual1.proximo
            atual2 = atual2.proximo
        
        return True

  def impares(self):
    impar = 0
    no_atual = self.cabeca

    while no_atual != None:

        if no_atual.dado % 2 != 0:
            impar += 1

        no_atual = no_atual.proximo
    
    return impar

  def pares(self):
    par = 0
    no_atual = self.cabeca

    while no_atual != None:

        if no_atual.dado % 2 == 0:
            par += 1

        no_atual = no_atual.proximo
    
    return par

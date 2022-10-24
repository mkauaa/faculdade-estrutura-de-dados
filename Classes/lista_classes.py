class Nodo:
  def __init__(self, dado = 0, proximo_nodo = None):
    self.dado = dado
    self.proximo = proximo_nodo
    
  def __repr__(self):
    return f'{self.dado} -> {self.proximo}'

class Lista:
  def __init__(self):
    self.cabeca = None
    self.cauda = None
    self.tamanho = 0
    
  def __repr__(self):
    return f'[{str(self.cabeca)}]'
  
  def vazia(self):
    if self.cabeca == None:
      return True
    else:
      return False
    
  def insereInicio(self, novo_dado):
    novo_nodo = Nodo(novo_dado)
    
    if self.vazia():
      self.cabeca = novo_nodo
      self.cauda = novo_nodo
      self.tamanho += 1
      
    else:
      novo_nodo.proximo = self.cabeca
      self.cabeca = novo_nodo
      self.tamanho += 1
      
  def insereFim(self, novo_dado):
    novo_nodo = Nodo(novo_dado)
  
    if self.vazia():
      self.cabeca = novo_nodo
      self.cauda = novo_nodo
      self.tamanho += 1
      
    else:
      self.cauda.proximo = novo_nodo
      self.cauda = novo_nodo
      self.tamanho += 1
  
  def remove(self, posicao):
    if self.vazia():
      return 'A lista está vazia.'
    
    if 0 <= posicao < self.tamanho:
      if posicao == 0:
        removido = self.cabeca.dado
        self.cabeca = self.cabeca.proximo
        
        self.tamanho -= 1
        
        if self.cabeca == None:
          self.cauda = None
          
        return removido
      
      else:
        atual = self.cabeca
        i = 0
        
        while i != posicao:
          anterior = atual
          atual = atual.proximo
          i += 1
          
        removido = atual.dado
        
        if atual == self.cauda:
          self.cauda = anterior
          
        anterior.proximo = atual.proximo
        self.tamanho -= 1
          
        return removido
      
    else:
      return 'Posição inválida.'
    
  def busca(self, dado):
    if self.vazia():
      return 'A lista está vazia.'
    
    else:
      atual = self.cabeca
      posicao = 0
      
      while atual.dado != dado:
        atual = atual.proximo
        posicao += 1
        
        if posicao == self.tamanho:
          return 'Dado não encontrado na lista.'
      
      return posicao

  def inserePosicao(self, novo_dado, posicao):
    if 0 <= posicao <= self.tamanho:
      if posicao == 0:
        self.insereInicio(novo_dado)
        self.tamanho += 1
      
      elif posicao == (self.tamanho):
        self.insereFim(novo_dado)
        self.tamanho += 1

      else:
        atual = self.cabeca
        i = 0
        
        while i != posicao:
          anterior = atual
          atual = atual.proximo
          i += 1
        
        # adaptar a partir daq
        removido = atual.dado
        
        if atual == self.cauda:
          self.cauda = anterior
          
        anterior.proximo = atual.proximo
        self.tamanho -= 1
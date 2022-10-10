from fila_classe import Fila
from Pilhas.pilha_classe import Pilha

fila = Fila()
pilha = Pilha()

for v in range(1, 6):
  print(fila)
  fila.insere(v)
  
for v in fila:
  pilha.insere(v)
  print(pilha)

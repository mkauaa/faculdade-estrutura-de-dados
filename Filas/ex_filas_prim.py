from Classes.fila_classe import Fila
from Classes.pilha_classe import Pilha

fila = Fila()
pilha = Pilha()

for v in range(1, 6):
  print(fila)
  fila.insere(v)
  
for v in fila:
  pilha.insere(v)
  print(pilha)

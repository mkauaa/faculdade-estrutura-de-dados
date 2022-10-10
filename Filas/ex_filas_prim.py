import sys
sys.path.append(".")

from Classes.fila_classe import Fila
from Classes.pilha_classe import Pilha

fila = Fila()
pilha = Pilha()

for v in range(1, 6):
  print(fila)
  fila.insere(v)
  
for v in range(1,6):
  pilha.insere(v)
  print(pilha)

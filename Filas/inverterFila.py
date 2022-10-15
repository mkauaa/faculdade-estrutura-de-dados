import sys
sys.path.append(".")

from Classes.fila_classe import Fila
from Classes.pilha_classe import Pilha

def inverterFila(f):
    pilha = Pilha()

    while not f.vazia():
        pilha.insere(f.remove())
    
    while not pilha.vazia():
        f.insere(pilha.remove())

    print(f)


fila = Fila()

for i in range(5):
    fila.insere(input(f"Insira o {i+1}º elemento da fila: "))

print(fila)

inverterFila(fila)


import sys
sys.path.append(".")

from Classes.fila_classe import Fila

def uniaoCrescente(f1, f2):
    f3 = Fila()
    
    while not f1.vazia() and not f2.vazia():
        if f1.cabeca.dado <= f2.cabeca.dado:
            f3.insere(f1.remove())
        
        else:
            f3.insere(f2.remove())

    while not f1.vazia():
        f3.insere(f1.remove())

    while not f2.vazia():
        f3.insere(f2.remove())

    return f3


fila = Fila()

for i in range(1, 9, 2):
    fila.insere(i)
    
print(fila)

fila2 = Fila()

for i in range(0, 9, 2):
    fila2.insere(i)
    
print(fila2)

print(uniaoCrescente(fila, fila2))

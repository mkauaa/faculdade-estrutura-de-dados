from fila_classe import Fila

f1 = Fila()
f2 = Fila()
f3 = Fila()
canal = Fila()

for i in range(3):
    f1.insere(input(f"Insira o {i+1}º elemento da fila: "))
    
for i in range(3):
    f2.insere(input(f"Insira o {i+1}º elemento da fila: "))

for i in range(3):
    f3.insere(input(f"Insira o {i+1}º elemento da fila: "))

print(f'Fluxo 1: {f1}')
print(f'Fluxo 2: {f2}')
print(f'Fluxo 3: {f3}')

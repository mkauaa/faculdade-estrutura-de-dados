import sys
sys.path.append(".")

from Classes.fila_classe import Fila

f1 = Fila()
f2 = Fila()
f3 = Fila()
canal = Fila()

i = 0
while True:
    valor = int(input(f"Insira o {i+1}º elemento do fluxo 1: "))
    f1.insere((valor, 1))  
     
    i += 1
    flag = int(input('Digite 1 para continuar ou 0 para concluir o fluxo: '))
    if flag == 0:
        break

i = 0
while True:
    valor = int(input(f"Insira o {i+1}º elemento do fluxo 1: "))
    f2.insere((valor, 2))

    i += 1 

    flag = int(input('Digite 1 para continuar ou 0 para concluir o fluxo: '))
    if flag == 0:
        break

i = 0
while True:
    valor = int(input(f"Insira o {i+1}º elemento do fluxo 1: "))
    f3.insere((valor, 3))

    i += 1

    flag = int(input('Digite 1 para continuar ou 0 para concluir o fluxo: '))
    if flag == 0:
        break

print(f'Fluxo 1: {f1}')
print(f'Fluxo 2: {f2}')
print(f'Fluxo 3: {f3}')

tamanho = f1.tamanho + f2.tamanho + f3.tamanho

for i in range(tamanho):
    if not f1.vazia():
        canal.insere(f1.remove())

    if not f2.vazia():
        canal.insere(f2.remove())

    if not f3.vazia():
        canal.insere(f3.remove())

print(f'Canal: {canal}')

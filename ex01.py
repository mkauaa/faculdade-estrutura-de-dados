# Questão 01. Fazer um programa para ler uma lista de 5 elementos, e, em seguida, mostrar
# a posição onde se encontram o maior e o menor valor e seus respectivos valores.

from random import randint

lista = []

cont = 0

while True:
    num = randint(1,10)

    if num not in lista:
        lista.append(num)
        cont += 1

    if cont == 5:
        break

numMaior = max(lista)
numMenor = min(lista)

indiceMaior = lista.index(numMaior)
indiceMenor = lista.index(numMenor)

print(f'Lista: {lista}')


print(f'O maior valor gerado foi {numMaior} e se encontra na posição {indiceMaior + 1}.')
print(f'O menor valor gerado foi {numMenor} e se encontra na posição {indiceMenor + 1}.')
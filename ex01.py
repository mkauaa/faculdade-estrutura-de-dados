# Questão 01. Fazer um programa para ler uma lista de 5 elementos, e, em seguida, mostrar
# a posição onde se encontram o maior e o menor valor e seus respectivos valores.

lista = [4, 3, 5, 2, 1]

maior = max(lista)
menor = min(lista)

for i, v in enumerate(lista):
    if v == maior:
        indiceMaior = i
    if v == menor:
        indiceMenor = i

print(f'O maior valor informado foi {maior} e se encontra na posição {indiceMaior + 1}')
print(f'O menor valor informado foi {menor} e se encontra na posição {indiceMenor + 1}')
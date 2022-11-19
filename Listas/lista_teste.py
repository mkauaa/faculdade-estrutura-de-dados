import sys
sys.path.append(".")

from Classes.lista_classes import Lista

lista = Lista()

if lista.vazia():
    print('\nA lista está vazia. Adicionando elementos...')

lista.insereInicio(1)
lista.insereInicio(2)
lista.insereFim(4)

print(lista)

print(f'A lista tem {lista.tamanho} elementos.')
print(f'Removendo o elemento "{lista.remove(1)}"...')

print(lista)

print(f'A lista tem {lista.tamanho} elementos.')

print(f'Procurando o elemento "4"... \nAchei! Na posição {lista.busca(4)}')

lista.inserePosicao(99, 1)

print(lista)
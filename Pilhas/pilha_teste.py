from Classes.pilha_classe import Pilha, Nodo

P = Pilha()
L = Pilha()

print('Pilha vazia: ', P)
P.remove()

for v in range(5):
    P.insere(v)
    print(f'Insere o valor {v} no topo da pilha: {P}')
    print(P.tamanho)

#for v in range(5):
#    P.remove()
#    print(f'Remove o valor do topo da pilha:   {P}')
#    print(P.tamanho)

for v in range(5):
    L.insere(v)
    print(f'Insere o valor {v} no topo da pilha: {L}')
    print(L.tamanho)
    
print(P.compara(L))

if P.compara(L):
  print('As pilhas são iguais.')

elif not P.compara(L):
  print('As pilhas são diferentes.')
    

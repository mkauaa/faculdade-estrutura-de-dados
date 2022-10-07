from classe_Nodo_Pilha import Pilha, Nodo

P = Pilha()

print('Pilha vazia: ', P)
P.remove()

for v in range(5):
    P.insere(v)
    print(f'Insere o valor {v} no topo da pilha: {P}')
    print(P.tamanho)

for v in range(5):
    P.remove()
    print(f'Remove o valor do topo da pilha:   {P}')
    print(P.tamanho)
    

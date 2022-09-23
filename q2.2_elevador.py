# Um elevador médio suporta 800Kg. Se a carga for excedida, as normas
# de segurança não serão cumpridas e há risco de acidentes. Suponha que o
# elevador esteja vazio e há várias pessoas na fila para entrar. Cada pessoa se pesa
# e, caso seja possível, entra no elevador. Se o peso de uma pessoa que deseja
# entrar exceder o que é possível transportar, então o elevador fecha as portas para
# ela e faz o trajeto com as que estão dentro. Escreva um algoritmo que simule a
# situação. Ou seja, deverá ler o peso de cada pessoa e emitir uma mensagem
# quando o peso for excedido. Informe ainda quantas pessoas estão sendo
# transportadas.

peso = 0
cont = 0

while True:
    pessoa = int(input(f'Informe o peso da {cont+1}ª pessoa: '))
    if peso + pessoa <= 800:
        peso += pessoa
        cont += 1
    
    else:
        print('\nOps! Peso máximo de 800kg excedido.\n')
        break

print(f'Transportando {cont} pessoas...\n')

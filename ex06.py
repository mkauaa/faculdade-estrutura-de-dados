# Questão 06. Adapte o programa anterior para executar a compra de vários clientes e ao
# solicitar o encerramento do dia, apresente o total arrecadado pelo restaurante.

dict = {1: ('Salada', 5.00), 2: ('Risoto', 10.50), 3: ('Picanha', 20.00)}

print('-' * 25 + '\n' + 'MENU'.center(25) + '\n' + '-' * 25)

for k, v in dict.items():
    print(f'({k}) {v[0]:^11} - R${v[1]:.2f}')

print('-' * 25)

cont = total = 0

while True:
    consumo = 0
    print(f'\n{cont + 1}º Cliente: ')

    while True:
        while True:
            opc = int(input('Informe seu pedido: '))

            if 1 <= opc <= 3:
                break
            else:
                print('Código inválido! Tente novamente. ')
            
        print(f'Você pediu um(a) {dict[opc][0]}. ')

        consumo += dict[opc][1]

        pedidoFlag = (str(input('\nDeseja pedir mais algo? (S/N) : '))).upper()

        if pedidoFlag != 'S':
            cont += 1
            break

        print()

    print(f'\nO total do {cont}º pedido equivale a R${consumo:.2f}.')

    total += consumo

    clienteFlag = (str(input('Encerrar o dia? (S/N) : '))).upper()

    if clienteFlag != 'N':
        break

print(f'\nO total arrecadado de {cont} pedidos equivale a R${total:.2f}.')
# Questão 05. Um restaurante do tipo buffet oferece cinco tipos básicos de comida.
# Cadastre-os com nome e valor. Após o cadastro, apresente um menu ao cliente para que
# escolha os pratos que deseja consumir. Dê ao cliente a opção de escolher quantos pratos
# ele desejar. Ao final apresente o valor do consumo do cliente. Utilize tuplas e/ou dicionário
# na resolução.

dict = {1: ('Salada', 5.00), 2: ('Risoto', 10.50), 3: ('Picanha', 20.00)}

consumo = 0

print('-' * 25 + '\n' + 'MENU'.center(25) + '\n' + '-' * 25)

for k, v in dict.items():
    print(f'({k}) {v[0]:^11} - R${v[1]:.2f}')

print('-' * 25)

while True:
    while True:
        opc = int(input('Informe seu pedido: '))

        if 1 <= opc <= 3:
            break
        else:
            print('Código inválido! Tente novamente. ')
        
    print(f'Você pediu um(a) {dict[opc][0]}. ')

    consumo += dict[opc][1]

    flag = (str(input('Deseja pedir mais algo? (S/N) : '))).upper()

    if flag != 'S':
        break

    print()

print(f'O total do pedido equivale a R${consumo:.2f}.')
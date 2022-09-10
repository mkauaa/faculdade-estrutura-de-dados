# Questão 02. Ler uma sequência de números reais e armazená-los. Determinar o maior
# elemento dessa sequência. A sequência termina quando for digitado o número (0) zero. Ao
# final, imprimir a lista resultante.

sequencia = list()

while True:
    num = float(input('Informe um número: '))
    if num == 0:
        break
    else:
        sequencia.append(num)

print('Devolvendo a sequência informada: ')

for num in sequencia:
    if num == max(sequencia):
        print(f'{num} (MAIOR!!)', end=', ')
    else:
        print(f'{num}', end=', ')
    if num == sequencia[-1]:
        print('FIM!')


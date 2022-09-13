# Questão 03. Dadas as temperaturas que foram registradas diariamente, 
# durante 4 semanas de um determinado mês, deseja-se:
# a) Determinar quais semanas possuíam pelo menos 3 dias com temperatura acima da média do mês.
# b) Quais as temperaturas mínima e máxima do mês em questão
# c) Crie um histograma da variação de temperatura da semana que obteve a temperatura máxima.

sem1 = [26, 29, 21, 27, 23, 25, 29]
sem2 = [21, 21, 23, 19, 24, 22, 21]
sem3 = [30, 29, 28, 30, 33, 29, 27]
sem4 = [24, 26, 25, 25, 27, 25, 24]

mes = sem1 + sem2 + sem3 + sem4

mediaMes = sum(mes) / len(mes)
maiorMes = max(mes)
menorMes = min(mes)

acima = [0, 0, 0, 0]

for temp in sem1:
    if temp > mediaMes:
        acima[0] += 1

for temp in sem2:
    if temp > mediaMes:
        acima[1] += 1

for temp in sem3:
    if temp > mediaMes:
        acima[2] += 1

for temp in sem4:
    if temp > mediaMes:
        acima[3] += 1

for cont in range(0, 4):
    print(f'A semana {cont + 1} teve {acima[cont]} temperaturas acima da média.')

print(f'\nA temperatura mínima do mês foi {menorMes} ºC, a máxima {maiorMes} ºC, e a média {mediaMes}.\n')

maiorDia = mes.index(maiorMes)

maiorSem = list()

if 0 <= maiorDia < 7:
    maiorSem = sem1[:]

if 7 <= maiorDia < 14:
    maiorSem = sem2[:]

if 14 <= maiorDia < 21:
    maiorSem = sem3[:]

if 21 <= maiorDia < 28:
    maiorSem = sem4[:]

diasSemana = ['D', 'S', 'T', 'Q', 'Q', 'S', 'S']

print('Histograma:\n')

for cont in range(0, 7):
    print(f'{diasSemana[cont]}: ', '■' * maiorSem[cont])

print()

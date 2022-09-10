# Questão 03. Dadas as temperaturas que foram registradas diariamente, 
# durante 4 semanas de um determinado mês, deseja-se:
# a) Determinar quais semanas possuíam pelo menos 3 dias com temperatura acima da média do mês.
# b) Quais as temperaturas mínima e máxima do mês em questão
# c) Crie um histograma da variação de temperatura da semana que obteve a temperatura
# máxima.

sem1 = [26, 29, 21, 27, 23, 25, 29]
sem2 = [21, 21, 23, 20, 24, 22, 21]
sem3 = [30, 29, 28, 30, 31, 29, 29]
sem4 = [24, 26, 25, 25, 27, 25, 24]

mes = sem1 + sem2 + sem3 + sem4

mediaMes = sum(mes) / len(mes)

acima = 0

inicio = 0
fim = 7

semana = 0

while semana <= 4:
    for dia, temp in enumerate(mes):
        if inicio < dia < fim:         
            if temp > mediaMes:
                acima += 1
            if acima > 3:
                print(f'A semana {semana} possui {acima} dias com temperatura acima da média do mês. ')        
    semana += 1 
    inicio += 7
    fim += 7
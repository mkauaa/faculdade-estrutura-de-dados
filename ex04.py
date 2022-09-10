# Questão 04. Escreva um programa que receba duas temperaturas e suas respectivas
# escalas (oC ou oF). Use tuplas para armazenar estas informações. A partir de então crie
# uma função que avalie qual das duas temperaturas é a maior. Perceba que se as
# temperaturas estiverem em escalas diferentes, a resposta deve ser dada na escala da
# segunda temperatura. ºF = ºC * 1.8 + 32

celsius = faren = 0

temp = float(input('Informe a 1º temperatura: '))
escala = (str(input('Informe a escala (C/ F) : º'))).upper()

tupla1 = (temp, escala)

temp = float(input('Informe a 2º temperatura: '))
escala = (str(input('Informe a escala (C/ F) : º'))).upper()

tupla2 = (temp, escala)

if tupla1[1] != tupla2[1]:
    if tupla2[1] == 'C':
        celsius = (tupla1[0] - 32) / 1.8

        if celsius > tupla2[0]:
            print(f'{celsius:.1f} ºC > {tupla2[0]} ºC')

        elif tupla2[0] > celsius:
            print(f'{tupla2[0]} ºC > {celsius:.1f} ºC')

    elif tupla2[1] == 'F':
        faren = (tupla1[0] * 1.8) + 32

        if faren > tupla2[0]:
            print(f'{faren:.1f} ºF > {tupla2[0]} ºF')

        elif tupla2[0] > faren:
            print(f'{tupla2[0]} ºF > {faren:.1f} ºF')

elif tupla1[1] == tupla2[1]:
    if tupla2[1] == 'C':
        if tupla2[0] > tupla1[0]:
            print(f'{tupla2[0]} ºC > {tupla1[0]} ºC')

        elif tupla1[0] > tupla2[0]:
            print(f'{tupla1[0]} ºC > {tupla2[0]} ºC')

    elif tupla2[1] == 'F':
        if tupla2[0] > tupla1[0]:
            print(f'{tupla2[0]} ºF > {tupla1[0]} ºF')

        elif tupla1[0] > tupla2[0]:
            print(f'{tupla1[0]} ºF > {tupla2[0]} ºF')
            
from exp_classe import verifica

while True:
    exp = str(input('Digite uma expressao aritmetica.: '))
    
    if verifica(exp) == True:
        print('A expressão informada é válida.')
    elif verifica(exp) == False:
        print('A expressao informada é inválida.')
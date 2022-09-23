# Crie um programa de adivinhação em que o usuário possa inserir um número até
# 10 para tentar adivinhar o número secreto sorteado pelo programa. O usuário 
# deverá ter 3 tentativas e a cada uma receberá uma dica se o número é maior
# ou menor do que o digitado. Após 3 erros, o usuário será informado da derrota
# e escolherá se deseja continuar jogando ou finalizar o programa.

from random import randint

print('== JOGO DA ADIVINHAÇÃO ==')
print(f'-> Você tem 3 tentativas.')

tentativa = 3
num = randint(1,10)

flag = 's'

while True:  
    chute = int(input('Informe um número inteiro natural menor que 10: '))

    if num != chute:
        tentativa -= 1
        print(f'\nErrado... Você tem {tentativa} tentativas.')

        if num < chute:    
            print(f'\nO número que eu pensei é menor que {chute}.')

        if num > chute:    
            print(f'\nO número que eu pensei é maior que {chute}.')

    else:
        print('\nVocê acertou!')
        
        flag = str(input('\nDeseja jogar novamente? [S/N]: '))

    if tentativa == 0:
        print(f'\nVocê perdeu!')
        tentativa = 3

        flag = str(input('\nDeseja jogar novamente? [S/N]: '))
        
    if flag in 'Nn':
            break

print('\nJogo encerrado. Tchau!\n')

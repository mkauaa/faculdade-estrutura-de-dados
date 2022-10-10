from pilha_classe import Pilha

def verifica(entrada):
    pilha = Pilha()
    for c in entrada:
        if c == '(' or c == '[' or c == '{':
            pilha.insere(c)
        elif c == ')' or c == ']' or c == '}':
            if pilha.vazia():
                return False
            if c == ')' and pilha.remove() !='(':
                return False
            elif c == ']' and pilha.remove() != '[':
                return False
            elif c == '}' and pilha.remove() != '{':
                return False

    if pilha.vazia():
        return True
    
    else:
        return False


# Principal

while True:
    exp = str(input('Digite uma expressao aritmetica.: '))
    
    if verifica(exp) == True:
        print('A expressão informada é válida.')
    elif verifica(exp) == False:
        print('A expressao informada é inválida.')
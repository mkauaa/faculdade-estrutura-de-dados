from class_pilha import Pilha

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

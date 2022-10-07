import re
from pilha_classe import Pilha

frase = str(input('Digite uma frase: '))

pilha = Pilha()

if frase[len(frase)-1] == '.':
  # re.sub substitui x caracteres por y caracter em string z
  frase = re.sub('[.!?]', '', frase)
  
  palavras = frase.split(' ')
  
  for palavra in palavras:
    
    for letra in palavra:
      pilha.insere(letra)
      
    string = ''
    
    while not pilha.vazia():
      string += pilha.remove()
      
    print(string, end=' ')
    
else:
  print("A frase não termina com '.'")
    

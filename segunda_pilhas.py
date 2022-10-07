from pilha_classe import Pilha

def padraoXY(string):
  
  if len(string) % 2 != 0:
    return False
  
  else:
    string1 = string[:len(string)//2]
    string2 = string[len(string)//2:]
    
    pilha = Pilha()
    
    for letra in string1:
      
      pilha.insere(letra)
    
    print(string1, string2)
    
    for letra in string2:
      
      if letra != pilha.remove():
        return False
    
    
    return True
  

# Principal

string = input('Digite uma palavra: ')

if padraoXY(string):
  print('É um palíndromo.')
  
elif not padraoXY(string):
  print('Não é um palíndromo.')

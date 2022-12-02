def bubblesort(lista):
    while True:
        flag = False

        for i in range(len(lista)):
            if i + 1 < len(lista) and lista[i] > lista[i+1]:
                auxiliar = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = auxiliar
                flag = True

        if flag == False:
            break

    return lista

L1 = [9, 4, 1, 2, 7]
L2 = [("Carlos", 70), ("João", 20), ("Cris", 40)]

print(bubblesort(L1))
print(bubblesort(L2))

def selectionsort(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[i]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

    return lista

print(selectionsort(L1))
print(selectionsort(L2))

def insertionsort(lista):
    for i in range(1, len(lista)):
        j = i - 1

        while j >= 0 and lista[j] > lista[i]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
            j -= 1

    return lista

print(insertionsort(L1))
print(insertionsort(L2))

#def quicksort(lista):
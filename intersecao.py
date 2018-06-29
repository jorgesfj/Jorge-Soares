def remove_repetidos(lista3):
    l = []
    for i in lista3:
        if i not in l:
            l.append(i)
    l.sort()
    return l

cont = 0
lista = []
lista3 = []
while cont<40:
    cont +=1
    a = int(input())
    lista.append(a)
lista1 = lista[0:20]
lista2 = lista[20:40]
numero = 0
while numero<20:
    for i in range(len(lista1)):
        if lista1[numero] == lista2[i]:
            lista3.append(lista2[i])
    numero+=1
lista3 = remove_repetidos(lista3)
for i in range(len(lista3)):
    print(lista3[i])
    

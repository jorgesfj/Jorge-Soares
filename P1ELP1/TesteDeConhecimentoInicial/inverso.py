lista = []
a = 1
while a!='0':
    a = input()
    lista.append(a)
for i in range(len(lista)-1):
    a = lista[i]
    print(a[::-1])

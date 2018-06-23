lista = []
lista2 = []
lista3 = []
primeiro = int(input())
while len(lista)<primeiro:
    palavras = input()
    lista.append(palavras)
for i in range(len(lista)):
    a = lista[i]
    for i in range(len(a)):
        numer = ord(a[i])
        final = chr(numer+3)
        lista2.append(final)
inverter = lista2[::-1]
for i in range(len(inverter)):
    a = inverter[i]
    for i in range(len(a)):
        numer = ord(a[i])
        final = chr(numer-1)
        lista3.append(final)
cont = 0
for i in range(len(lista3)):
    cont +=1
    print(lista3[i],end='')

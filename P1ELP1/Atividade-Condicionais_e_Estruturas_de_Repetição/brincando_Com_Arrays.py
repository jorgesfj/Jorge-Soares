quantidade = int(input())

numeros = input()

print(numeros[::-1],'\n')
lista3 = []

lista = numeros.split()
for i in range(1,len(lista)):
	lista3.append(lista[i])
lista3.append(lista[0])
for i in range(len(lista3)):
	print(lista3[i],'', end = '')
print('\n')

lista2 = []
for i in range(len(lista)):
	lista2.append(int(lista[i]))

final = sorted(lista2, key=int, reverse=True)
for i in range(len(final)):
	print(final[i],'', end='')
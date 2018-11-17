numeros = input()
lista = []
soma = []
lista_numeros = numeros.split()
for i in range(len(lista_numeros)):
	lista.append(int(lista_numeros[i]))
for i in range(len(lista)):
	if (lista[i] > 0) and (lista[i]%2 == 0):
		soma.append(lista[i])
cont = 0
for i in range(len(soma)):
	cont += soma[i]

if cont == 0:
	print("-1")

else:
	print(cont/len(soma)) 
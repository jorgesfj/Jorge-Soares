n = int(input())
elementos = input()
lista = []
lista_elementos = []
lista_aux = elementos.split()
for i in range(len(lista_aux)):
	lista_elementos.append(int(lista_aux[i]))
for i in range(0,n):
	if i+1 < n:
		razao = lista_elementos[i] - lista_elementos[i+1]
		lista.append(razao)
	else:
		break
print(lista)
cont = 1
for i in range(len(lista)):
	if i+1 < len(lista):
		if lista[i] != lista[i+1]:
			cont += 1
print(cont)
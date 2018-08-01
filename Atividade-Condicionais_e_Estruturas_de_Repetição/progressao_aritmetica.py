n = int(input())
elementos = input()
lista = []
dicionario = {}
lista_elementos = []
lista_aux = elementos.split()
for i in range(len(lista_aux)):
	lista_elementos.append(int(lista_aux[i]))
for i in range(0,n):
	if i+1 < n:
		razao = lista_elementos[i] - lista_elementos[i+1]
		dicionario[razao] = razao
	else:
		break

print(len(dicionario))
n = int(input())
elementos = input()
lista = []
lista_auxiliar2 = []
dicionario = {}
cont = 0
lista_elementos = []
lista_aux = elementos.split()
for i in range(len(lista_aux)):
	lista_elementos.append(int(lista_aux[i]))
for i in range(0,n):
	if i+1 < n:
		razao = lista_elementos[i] - lista_elementos[i+1]
		dicionario[razao] = razao
		lista_auxiliar2.append(razao)
	else:
		break
for i in range (len(lista_auxiliar2)):
		if lista_auxiliar2.count(lista_auxiliar2[i]) > 1 :
			cont += 1
print(len(dicionario))
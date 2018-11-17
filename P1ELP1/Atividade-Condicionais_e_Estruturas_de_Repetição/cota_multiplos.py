primeiro = int(input())
segundo = int(input())
primeira_lista = []
segunda_lista = []
lista = []
for i in range(1,50):
	if (i*primeiro) < 50:
		primeira_lista.append(i*primeiro)
	else:
		break

for i in range(1,50):
	if (i*segundo) < 50:
		segunda_lista.append(i*segundo)
	else:
		break
for i in range(len(primeira_lista)):
	aux = primeira_lista[i]
	for x in range(len(segunda_lista)):
		aux2 = segunda_lista[x]
		if aux == aux2 and aux not in lista:
			lista.append(aux)
print(len(lista))
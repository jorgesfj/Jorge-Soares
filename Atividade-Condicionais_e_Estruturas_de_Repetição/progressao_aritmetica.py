def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l


n = int(input())
lista_aux = list(map(int,input().split()))
lista_auxiliar2 = []
dicionario = {}
lista_elementos = []
for i in range(len(lista_aux)):
	lista_elementos.append(lista_aux[i])
for i in range(0,n):
	if i+1 < n:
		razao = lista_elementos[i] - lista_elementos[i+1]
		dicionario[razao] = razao
		lista_auxiliar2.append(razao)
	else:
		break
lista_auxiliar2.append(0)
cont = 0
for i in range(len(lista_auxiliar2)):
	if i+1 <= len(lista_auxiliar2)-1:
		if lista_auxiliar2.count(lista_auxiliar2[i]) > 1 and lista_auxiliar2[i]!=lista_auxiliar2[i+1]:
			cont +=1
	if len(remove_repetidos(lista_auxiliar2)) == 1:
		cont = 1
			
print(lista_auxiliar2)
print(cont)


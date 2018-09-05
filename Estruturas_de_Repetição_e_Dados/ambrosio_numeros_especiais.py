n,q = list(map(int,input().split()))
array = list(map(int,input().split()))
cont = 0
k = 0
lista = []
while cont<q:
	cont+=1
	a = list(map(int,input().split()))
	lista.append(a)
fim = []
for i in range(len(lista)):
	for x in range(0,len(lista[i]),3):
		if lista[i][0] == 1:
			aux = 0
			for w in range(lista[i][1]-1,lista[i][2]):
				teste = str(array[w])
				if len(teste) <1 or teste[0] == teste[len(teste)-1]:
					aux +=1
			fim.append(aux)
		if lista[i][0] == 2:
			k = lista[i][2]
			auxiliar = (lista[i][1]) -1
			array[auxiliar] = k
			

for i in range(len(fim)):
	print(fim[i])
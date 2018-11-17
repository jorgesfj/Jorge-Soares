n,m = list(map(int,input().split()))
substituicao = []
while n!= 0 and m!=0:
	cont = 0
	while cont<n:
		a,b,c= list(map(str,input().split()))
		substituicao.append(a)
		substituicao.append(c)
		cont+=1
	cont = 0
	lista = []
	while cont<m:
		texto = input()
		lista.append(texto)
		cont+=1
	lista2 = []
	for i in range(len(lista)):
		lista2.append(lista[i].split())
	for i in range(len(lista2)):
		for j in range(len(lista2[i])):
			for w in range(0,len(substituicao),2):
				if substituicao[w] == lista2[i][j]:
					lista2[i][j] = substituicao[w+1]

	for w in range(len(substituicao[w])):
		if len(substituicao[w]) == 1:
			for i in range(len(lista2)):
				for x in range(len(lista2[i])):
					for b in range(len(lista2[i][x])):
						if lista2[i][x][b] == substituicao[w]:
							lista2[i][x][b] = substituicao[w]



							
	for i in range(len(lista2)):
		for j in range(len(lista2[i])):
			print(lista2[i][j], end =" ")
		print("\n")
	substituicao = []
	n,m = list(map(int,input().split()))
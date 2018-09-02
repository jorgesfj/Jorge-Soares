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
	n,m = list(map(int,input().split()))
lista2 = []
for i in range(len(lista)):
	lista2.append(lista[i].split())
lista3 = []
for i in range(len(lista2)):
	for j in range(len(lista2[i])):
		lista3.append(lista2[i][j])
for i in range(len(lista3)):
	for j in range(0,len(substituicao)-1,2):
		if lista3[i] == substituicao[j]:
			lista3[i] = substituicao[j+1]
lista_num = []
aux = 0
for i in range(len(lista2)):
	aux+= len(lista2[i])
	lista_num.append(aux)
while len(lista_num)<len(lista3):
	lista_num.append(0)
print(lista_num)

for i in range(len(lista3)):
	print(lista3[i], end=" ")
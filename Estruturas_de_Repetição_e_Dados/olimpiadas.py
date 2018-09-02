n,m = list(map(int, input().split()))
contador = 0
dic_o = {}
dic_p = {}
dic_b = {}
vencedores = []
while contador<n:
	contador+=1
	o,p,b = list(map(int,input().split()))
	dic_o[contador] = o
	dic_p[contador] = p
	dic_b[contador] = b
for item in sorted(dic_o, key = dic_o.get, reverse = True):#ordenar o dicionario de acordo com o item
	vencedores.append(item)#oque interessa pra questão é a posição e não a quantidade de medalhas
#Até aqui ele so testa para ouro. Se não ouver impate isso é o que ele deve imprimir
#=====================================================================================================#
cont = 0
for j in range(1,len(dic_o)):
	aux = dic_o[j]
	for i in range(1,len(dic_o)):
		if aux == dic_o[i]:
			cont+=1
if cont <=1:
	for i in range(len(vencedores)):
		print(vencedores[i])

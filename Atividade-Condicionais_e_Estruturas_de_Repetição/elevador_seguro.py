peso = int(input())
cont = 1
pesos = []
pesos.append(peso)
som = peso
while cont<7 and peso!=0 and som < 560:
	peso = int(input())
	som += peso
	pesos.append(peso)
	cont +=1
if cont>=7:
	print("Limite de pessoas atingido")
soma = 0
cont2 = 0
for i in range(len(pesos)):
	if (soma + pesos[i])<560:
		soma += pesos[i]
		cont2+=1
	else:
		break
print(' {}\n{}'.format(cont2,soma))
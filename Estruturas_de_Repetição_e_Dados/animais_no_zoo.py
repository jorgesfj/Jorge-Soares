especie = input()
peso = float(input())
pais = input()
continuador = input()

contadorm = 0
contadorc = 0
listat = []


if especie.upper() == "MACACO":
	contadorm +=1
elif especie.upper() == "COBRA" and pais.upper == "VENEZUELA":
	contadorc+=1
elif especie.upper() == "TIGRE":
	listat.append(peso)

while continuador.upper() != "PARAR":

	especie = input()
	peso = float(input())
	pais = input()
	continuador = input()


	if especie.upper() == "MACACO":
		contadorm +=1
	elif especie.upper() == "COBRA" and pais.upper == "VENEZUELA":
		contadorc+=1
	elif especie.upper() == "TIGRE":
		listat.append(peso)
 	
print(contadorm)

if len(listat)>0:
	print("{:.2f}".format(sum(listat)/len(listat)))
else:
	print("{:.2f}".format(len(listat)))





print(contadorc)
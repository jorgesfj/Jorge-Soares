romano = input()
lista = []
lista_int = []
for i in range(len(romano)):
	lista.append(romano[i])
for i in range(len(lista)):
	if lista[i] == 'I':
		lista_int.append(int('1'))
	if lista[i] == 'V':
		lista_int.append(int('5'))
	if lista[i] == 'X':
		lista_int.append(int('10'))
	if lista[i] == 'L':
		lista_int.append(int('50'))
	if lista[i] == 'C':
		lista_int.append(int('100'))
	if lista[i] == 'D':
		lista_int.append(int('500'))
	if lista[i] == 'M':
		lista_int.append(int('1000'))

if len(lista_int)>=2:
	if lista_int[0]>=lista_int[1]:
			subtra = sum(lista_int)
	else:
		lista_int.sort(key=int, reverse=True)
		subtra = lista_int[0]
		for i in range(1,len(lista_int)):
			subtra = subtra - lista_int[i]
else:
	subtra = lista_int[0]



if subtra%5 == 0:
	print("O numero é multiplo de 5")
else:
	var = subtra%5
	print("O resto pela divisao por 5 do numero dado e igual a {}!".format(var))
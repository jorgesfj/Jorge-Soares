romano = input()
lista = []
lista_int = []
lista.append('a')
for i in range(len(romano)):
	lista.append(romano[i])
for i in range(len(lista)):
	if lista[i] == 'I':
		if i+1 <len(lista):
			if lista[i+1] == 'V':
				lista_int.append(int('-1'))
			elif lista[i+1] == 'V':
				lista_int.append(int('-1'))
			else:
				lista_int.append(int('1'))
		else:
			lista_int.append(int('1'))
	elif lista[i] == 'V':
		if i+1 <len(lista):
			if lista[i+1] == 'X':
				lista_int.append(int('-5'))
			else:
				lista_int.append(int('5'))
		else:		
			lista_int.append(int('5'))
	elif lista[i] == 'X':
		if i+1 <len(lista):
			if lista[i+1] == 'L':
				lista_int.append(int('-10'))
			else:
				lista_int.append(int('10'))
		else:
			lista_int.append(int('10'))
	elif lista[i] == 'L':
		if i+1 <len(lista):
			if lista[i+1] == 'C':
				lista_int.append(int('-50'))
			else:
				lista_int.append(int('50'))
		else:
			lista_int.append(int('50'))
	elif lista[i] == 'C':
		if i+1 <len(lista):
			if lista[i+1] == 'D':
				lista_int.append(int('-100'))
			else:
				lista_int.append(int('100'))
		else:
			lista_int.append(int('100'))
	elif lista[i] == 'D':
		if i+1 <len(lista):
			if lista[i+1] == 'M':
				lista_int.append(int('-500'))
			else:
				lista_int.append(int('500'))
		else:
			lista_int.append(int('500'))
	elif lista[i] == 'M':
		lista_int.append(int('1000'))
soma = 0
for i in range(len(lista_int)):
	soma += lista_int[i]


if soma%5 == 0:
	print("O numero é multiplo de 5")
else:
	var = soma%5
	print("O resto pela divisao por 5 do numero dado e igual a {}!".format(var))
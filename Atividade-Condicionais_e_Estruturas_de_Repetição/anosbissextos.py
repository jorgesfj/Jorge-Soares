anos = input()
lista = anos.split()
lista_anos = []
ano1 = int(lista[0])
ano2 = int(lista[1])
for i in range(ano1 - 1,ano2):
	if i%1000 == 0:
		lista_anos.append(i)
	if (i%4 ==0 and i%100 !=0) or (i%4 !=0 and i%400 == 0) :
		lista_anos.append(i)
for i in range(len(lista_anos)):
	print(lista_anos[i])
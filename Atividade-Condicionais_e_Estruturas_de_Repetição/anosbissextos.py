anos = input()
lista = anos.split()
lista_anos = []
cont = 0
ano1 = int(lista[0])
ano2 = int(lista[1])
for i in range(ano1,ano2):
	if i%1000 == 0:
		cont +=1
		lista_anos.append(i)
	if (i%4 ==0 and i%100 !=0) or (i%4 !=0 and i%400 == 0) :
		lista_anos.append(i)
		cont +=1
if cont == 0:
	print("-1")
else:
	for i in range(len(lista_anos)):
		print(lista_anos[i])
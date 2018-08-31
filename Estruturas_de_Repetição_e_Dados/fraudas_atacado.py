lista = []
idade = int(input())
if idade<=2:
	qnt = 9*30
else:
	qnt = 6*30
lista.append(qnt)
continuador = input()

while continuador.upper() != "NÃO":
	idade = int(input())
	if idade<=2:
		qnt = 9*30
	else:
		qnt = 6*30
	lista.append(qnt)
	continuador = input()
print(lista)
if sum(lista)%100 ==0:
	print(sum(lista)//100)
	print('0')
else:
	print((sum(lista)//100)+1)
	print(100 - (sum(lista)%100) )

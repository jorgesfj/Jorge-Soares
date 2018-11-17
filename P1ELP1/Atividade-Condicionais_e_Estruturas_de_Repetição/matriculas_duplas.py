programacao_II = input()
programacao_III = input()
lista_fim = []
listaII = programacao_II.split()
listaIII = programacao_III.split()
for i in range (len(listaII)):
	aux1 = listaII[i]
	for j in range(len(listaIII)):
		aux2 = listaIII[j]
		if aux1 == aux2:
			lista_fim.append(aux1)
for i in range(len(lista_fim)):
	print(lista_fim[i], end =" ")
def conta_ocorrencias(s):
    ocorrencias = {}
    for c in s:
        if c in ocorrencias:
            ocorrencias[c] = ocorrencias[c] + 1
        else:
            ocorrencias[c] = 1
    return ocorrencias








l,u = list(map(int,input().split()))
lista = [l]
lista_primos =[]
for i in range(l,u+1):
	numero = i
	divisores = 0
	for divisor in range(1, numero):
		if numero % divisor == 0:
			divisores = divisores + 1
		if divisores > 1:
			break
	if divisores <= 1:
  		lista_primos.append(i)
lista_saltos = []
for i in range(0,len(lista_primos)-1):
	saltos = lista_primos[i+1] - lista_primos[i]
	lista_saltos.append(saltos)
aux = -1
dic_o = conta_ocorrencias(lista_saltos)
for item in sorted(dic_o, key = dic_o.get, reverse = True):
	aux = item
	break
print(aux)
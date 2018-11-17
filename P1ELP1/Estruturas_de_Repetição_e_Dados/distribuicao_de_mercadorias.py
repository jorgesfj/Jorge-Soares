n = int(input())
cont= 0
carga =[]
tipo_entrega = []
distancia = []
while cont < n:
	cont+=1
	p = float(input())
	carga.append(p)
	e = int(input())
	tipo_entrega.append(e)
	d = float(input())
	distancia.append(d)
qnt_caminhoes = []
valor = []
qnt = 0
for i in range(len(carga)):
	if tipo_entrega[i] == 0:
		if carga[i]%10 == 0:
			qnt = carga[i]/10
			qnt_caminhoes.append(qnt)
		else:
			qnt = (carga[i]//10)+1
			qnt_caminhoes.append(qnt)
		preco = qnt*500
		valor.append(preco)
	else:
		if carga[i]%5 == 0:
			qnt = carga[i]/5
			qnt_caminhoes.append(qnt)
		else:
			qnt = (carga[i]//5)+1
			qnt_caminhoes.append(qnt)
		preco = qnt*1200
		valor.append(preco)



aux = 0
for i in range(len(distancia)):
	if max(distancia)==distancia[i]:
		aux = i
	


maior_tempo = 0
if tipo_entrega[aux] == 0:
	if max(distancia)%100 == 0:
		maior_tempo = max(distancia)/100
	else:
		maior_tempo = (max(distancia)/100)+1
else:
	if max(distancia)%250 ==0:
		maior_tempo = max(distancia)/250
	else:
		maior_tempo = (max(distancia)/250)+1

print("{:.0f} {:.0f} {:.0f}\n".format(sum(qnt_caminhoes),sum(valor),maior_tempo))
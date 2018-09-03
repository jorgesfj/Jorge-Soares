vida = 100
dano_total = 0
dano_total_lista = []
tempo = []
danos = int(input())
cont = 0
while cont<danos and aux<100:
	cont+=1
	x,y = list(map(int,input().split()))
	aux = x
	dano_total += x
	dano_total_lista.append(x)
	tempo.append(y)
regeneracao = int(input())

vida -= dano_total
for i in range(0,tempo[len(tempo)-1]):
	if vida<100:
		vida+=5
aux = 0
for i in range(len(dano_total_lista)):
	if dano_total_lista[i] >=100:
		aux +=1
if aux>=1:
	print("Inimigo Morto")
else:
	if vida>0:
		print("Inimigo Vivo")
	else:
		print("Inimigo Morto")
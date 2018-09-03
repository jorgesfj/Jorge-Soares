vida = 100
dano_total = 0
tempo = []
danos = int(input())
cont = 0
while cont<danos:
	cont+=1
	x,y = list(map(int,input().split()))
	dano_total += x
	tempo.append(y)
regeneracao = int(input())

vida -= dano_total
for i in range(0,tempo[len(tempo)-1]):
	if vida<100:
		vida+=5
if vida>0:
	print("Inimigo Vivo")
else:
	print("Inimigo Morto")
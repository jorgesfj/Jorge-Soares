var = input().split()
n = int(var[0])
m = int(var[1])
lista = []

for i in range(n):
	lista.append([0,0,0])

dic = {}

def addnalista(listalocal):
	lista[int(local[0])-1][0]+=1
	lista[int(local[1])-1][1]+=1
	lista[int(local[2])-1][2]+=1

for i in range(n):
	try:
		local = input().split()
		addnalista(local)
	except:
		pass

for i in range(n):
	dic[i+1]=str(lista[i][0])+str(lista[i][1])+str(lista[i][2])

for item in sorted(dic,key = dic.get, reverse = True):
	print(item)
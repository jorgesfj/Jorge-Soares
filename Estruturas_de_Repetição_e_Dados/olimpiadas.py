n,m = list(map(int, input().split()))
contador = 0
dic_o = {}
dic_p = {}
dic_b = {}
vencedores = []
while contador<n:
	contador+=1
	o,p,b = list(map(int,input().split()))
	dic_o[contador] = o
	dic_p[contador] = p
	dic_b[contador] = b

i = 1
if i+1 < n:
	i+=1
	for item in sorted(dic_o, key = dic_o.get, reverse = True):
		if dic_o[item]!= dic_o[item+1]:
			print(item)
		elif dic_p[item]!=dic_p[item+1]:
			for item in sorted(dic_p, key = dic_p.get, reverse = True):	
				print(item)
		elif dic_b[item] != dic_b[item+1]:
			for item in sorted(dic_b, key = dic_b.get, reverse = True):
				print(item)
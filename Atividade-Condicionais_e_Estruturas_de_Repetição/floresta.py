n = int(input())
cont = 0 
eucaliptos = (n/2) + 1 
eucaliptos = int(eucaliptos)
numero = n - eucaliptos
for j in range(1,n):
	for w in range(1,n):
		if (j*w) + eucaliptos == n:
			cont +=1
print(cont)
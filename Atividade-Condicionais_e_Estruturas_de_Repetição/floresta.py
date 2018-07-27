n = int(input())
cont = 0
for i in range(n//2,0,-1):
	aux = n - i
	if aux%2 == 0:
		cont +=1
print(cont//3)
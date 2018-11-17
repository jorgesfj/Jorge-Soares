def pares(n):
	n -= 1
	if n>0:
		pares(n)
	if n%2 ==0:
		print(n)
n = int(input())
n +=1
pares(n)
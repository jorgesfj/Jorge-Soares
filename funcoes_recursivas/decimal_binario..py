def binario(n):
	resto = n%2
	n = int(n/2)
	if n>0:
		binario(n)
	print(resto)

n = int(input())
binario(n)
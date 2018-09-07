def fact(n):
	fat = 1
	for i in range(n,1,-1):
		fat *= i
	return fat  
def comb(n,d):
	if d != 0:
		comb = fact(n)/(fact(d)*fact((n-d)))
	else:
		comb = 2
	return comb
n = int(input())
d = int(input())
print(comb(n,d))
#nao consegui fazer
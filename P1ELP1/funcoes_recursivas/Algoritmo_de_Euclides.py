def euclides(a,d):
	a = max(c,d)
	b = min(c,d)
	if(a%b == 0):
		return b
	else:
		return euclides(b,(a%b))

n = int(input())
cont = 0
while cont<n:
	cont+=1
	c,d = list(map(int,input().split()))
	print("MDC({},{}) = {}".format(c,d,euclides(c,d)))
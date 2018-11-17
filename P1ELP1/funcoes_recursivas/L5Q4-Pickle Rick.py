def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
a = 1
b = 1
fib = a+b
n = int(input())
if fibonacci(n)<=1:
	print("O antidoto nao e necessario")
else:
	print("{} mg/L".format(fibonacci(n)))

texto = input()
a = 0
for i in range(len(texto)):
	if texto[i] == "[":
		a=1
	elif texto[i] == "]": 
		a=1
	else:
		print(texto[i], end="")
print("\n")

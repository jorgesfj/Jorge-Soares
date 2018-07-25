def vogal(letra):
	vogais = "aeiouAEIOU"
	if letra.lower() not in vogais:
		return True
	return False





palavras  = input()
lista_palavra = palavras.split()
primeira = lista_palavra[0]
segunda = lista_palavra[1]
palavrafinal = ''
if len(primeira)!= len(segunda):
	print("ERRO")
else:
	for i in range(len(primeira)):
		if primeira[i] == segunda[i] and vogal(primeira) and vogal(segunda):
			palavrafinal += str(i)
		elif i%2 == 0:
			palavrafinal += primeira[i].upper()
		else:
			palavrafinal +="!!"
print(palavrafinal)
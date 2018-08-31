especie_do_animal = input()
peso_animal = float(input())
pais_de_origem = input()
continuador = input()
lista = []
contador_macacos = 0
contador_cobras_venezuelanas = 0




if especie_do_animal == "macaco":
		contador_macacos+=1
elif pais_de_origem == "Venezuela" and especie_do_animal == "cobra":
	contador_cobras_venezuelanas +=1
elif especie_do_animal == "tigre":
	lista.append(peso_animal)


while continuador == "continuar":
	especie_do_animal = input()
	peso_animal = float(input())
	pais_de_origem = input()
	continuador = input()
	
	if especie_do_animal == "macaco":
		contador_macacos+=1
	elif pais_de_origem == "Venezuela" and especie_do_animal == "cobra":
		contador_cobras_venezuelanas +=1
	elif especie_do_animal == "tigre":
		lista.append(peso_animal)


print(contador_macacos)
if len(lista)>0:
	print("{:.2f}".format(sum(lista)/len(lista)))
else:
	print("{:.2f}".format(len(lista)))
print(contador_cobras_venezuelanas)
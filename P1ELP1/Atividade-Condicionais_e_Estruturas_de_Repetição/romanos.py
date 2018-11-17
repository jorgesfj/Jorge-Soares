n = input()
arabicos = []
nums = {'M':1000,

'D':500,

'C':100,

'L':50,

'X':10,

'V':5,

'I':1}

for i in range(len(n)):
	if n[i] in nums:
		arabicos.append(int(nums[n[i]]))

suma = int(arabicos[len(arabicos)-1])
for i in range(len(arabicos)-2,-1,-1):
	if arabicos[i]<suma:
		suma -= arabicos[i]
	if arabicos[i]>=suma:
		suma += arabicos[i]

if suma%5 == 0:
	print("O numero é multiplo de 5")
else:
	var = suma%5
	print("O resto pela divisao por 5 do numero dado e igual a {}!".format(var))
cont = 0
lista_nome = []
lista_nome_min = []
while cont <10:
  cont+=1
  nomes = input()
  lista_nome_min.append(nomes)
  nomes = nomes.upper()
  lista_nome.append(nomes)
letra = input()
letra = letra.upper()
lista_fim = []
for i in range(len(lista_nome)):
  aux = lista_nome[i]
  for j in range(len(aux)):
    if aux[j] == letra:
      lista_fim.append(lista_nome_min[i])
for i in range(len(lista_fim)):
  print(lista_fim[i])
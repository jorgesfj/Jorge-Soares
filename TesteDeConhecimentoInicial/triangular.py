n = int(input())
cont = 1
while cont * (cont+1) * (cont+2) < n:
    cont += 1
if cont * (cont+1) * (cont+2) == n:
    print('''Verdadeiro
{}*{}*{} = {}''' .format(cont,cont+1,cont+2,n))
else:
    print("Falso")

cont = 0
tam = input()
tam = tam.split()
k_n = input()
k_n = k_n.split()
lista_a = input()
lista_a = lista_a.split()
lista_b = input()
lista_b = lista_b.split()
menor = int(k_n[0])
for i in range(0,int(k_n[0])):
    aux = lista_a[i]
    for i in range(0,int(k_n[1])):
        if aux<lista_b[i]:
            cont+=1
        else:
            cont = 0
if cont>=menor:
    print("YES")
else:
    print("NO")

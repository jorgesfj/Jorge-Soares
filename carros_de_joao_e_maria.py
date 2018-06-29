def maior (lista):
    for i in range(len(lista)):
        aux = lista[i]
        for i in range(len(lista)):
            if aux<lista[i]:
                aux = lista[i]
    return aux
def media(lista):
    cont = 0
    for i in range(len(lista)):
        cont +=lista[i]
    media = cont/len(lista)
    return media
y = 0
lista_ano = []
lista_velocidade = []
continuar = input()
if continuar == 'n':
        y = 1
        x = 0
elif continuar == 'N':
        y = 1
        x = 0
else:
    x=1
while x==1:
    ano = int(input())
    lista_ano.append(ano)
    velocidade = float(input())
    lista_velocidade.append(velocidade)
    continuar = input()
    if continuar == 'n':
        x= 0
    elif continuar == 'N':
        x= 0
    
if y==0:
    print('{}\n{}\n{}'.format(maior(lista_velocidade),maior(lista_ano),media(lista_velocidade)))
else:
    print('zero')

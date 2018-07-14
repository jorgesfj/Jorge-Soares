def soma (lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l


def decomposicao(n):          
    lista=[]                 
    for i in range(2,n): 
        while n%i==0:    
            n=n/i        
            lista.append(i)  
    if soma(lista)==0:        
        lista.append(n)      
    return lista

def verificacao(lista):
    pi = 0
    lista2 = []
    for i in range(len(lista)):
        lista2.append(lista.count(lista[i]))
    return lista2

def final (x):
    lista = decomposicao(x)
    resultado = []
    lista2 = verificacao(lista)
    for i in range(len(lista)):
        if lista2[i]>1:
            resultado.append(lista2[i]*lista[i])
        else:
            resultado.append(lista[i])
    resultado = remove_repetidos(resultado)
    return soma(resultado)

x = int(input())
while x!=0:
    print(final(x))
    x = int(input())
    

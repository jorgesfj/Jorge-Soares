num = input()
lista = num.split()
n1 = float(lista[0])
n2 = float(lista[1])
if n1 == n2 == 0:
    print('Origem')
elif n1 == 0 and n2 != 0:
    print('Eixo Y')
elif n2 == 0 and n1 != 0:
    print('Eixo X')
elif n1<0 and n2<0:
    print('Q3')
elif n1>0 and n2>0:
    print('Q1')
elif n1>0 and n2<0:
    print('Q4')
elif n1<0 and n2>0:
    print('Q2')

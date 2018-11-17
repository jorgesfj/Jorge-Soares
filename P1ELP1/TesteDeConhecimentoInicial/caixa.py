dinheiro = float(input())
notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0
moedas_1 = 0
moedas_50 = 0
moedas_25 = 0
moedas_10 = 0
moedas_05 = 0
moedas_01 = 0
if dinheiro >= 100:
    notas_100 = dinheiro//100
    dinheiro = dinheiro - (notas_100 *100)
if dinheiro >= 50:
    notas_50 = dinheiro//50
    dinheiro = dinheiro - (notas_50 *50)
if dinheiro >= 20:
    notas_20 = dinheiro//20
    dinheiro = dinheiro - (notas_20 *20)
if dinheiro >= 10:
    notas_10 = dinheiro//10
    dinheiro = dinheiro - (notas_10 *10)
if dinheiro >= 5:
    notas_5 = dinheiro//5
    dinheiro = dinheiro - (notas_5 *5)
if dinheiro >= 2:
    notas_2 = dinheiro//2
    dinheiro = dinheiro - (notas_2 *2)
if dinheiro >= 1:
    moedas_1 = dinheiro//1
    dinheiro = dinheiro - (moedas_1)
if dinheiro >= 0.5:
    moedas_50 = dinheiro//0.5
    dinheiro = dinheiro - (moedas_50*0.5)
if dinheiro >= 0.25:
    moedas_25 = dinheiro//0.25
    dinheiro = dinheiro - (moedas_50*0.25)
if dinheiro >= 0.10:
    moedas_10 = dinheiro//0.10
    dinheiro = dinheiro - (moedas_10*0.10)
if dinheiro >= 0.05:
    moedas_05 = dinheiro//0.05
    dinheiro = dinheiro - (moedas_05*0.05)
if dinheiro >= 0.01:
    moedas_01 = dinheiro//0.01


print('''NOTAS:
{} nota(s) de R$ 100.00
{} nota(s) de R$ 50.00
{} nota(s) de R$ 20.00
{} nota(s) de R$ 10.00
{} nota(s) de R$ 5.00
{} nota(s) de R$ 2.00
MOEDAS:
{} moeda(s) de R$ 1.00
{} moeda(s) de R$ 0.50
{} moeda(s) de R$ 0.25
{} moeda(s) de R$ 0.10
{} moeda(s) de R$ 0.05
{} moeda(s) de R$ 0.01'''.format(int(notas_100),int(notas_50),int(notas_20),int(notas_10),int(notas_5),int(notas_2),int(moedas_1),int(moedas_50),int(moedas_25),int(moedas_10),int(moedas_05),int(moedas_01)))

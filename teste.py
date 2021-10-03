import os

taxa=0.04
tempo=3
C=20000
divisao=8

Saldo_Devedor1=C*(1+taxa)**tempo

J1=Saldo_Devedor1-C

parcela1=Saldo_Devedor1/8
Saldo_devedor2=Saldo_Devedor1-parcela1
os.system('cls')

print('Saldo devedor 1: ',round(Saldo_Devedor1,2))
print('Parcela: ',round(parcela1, 2),'     Juros: ', round((J1/8), 2))
print('Saldo devedor 2: ',round(Saldo_devedor2,2))
print('=============================================')

Saldo_devedor3=(Saldo_devedor2-parcela1)*(1+taxa)
parcela2=Saldo_devedor2/7

print('Saldo devedor 2: ',round(Saldo_devedor2,2))
print('Parcela: ',round(parcela2, 2),'     Juros: ', round((J1/7), 2))
print('Saldo devedor 3: ',round(Saldo_devedor3,2))
print('=============================================')

Saldo_devedor4=(Saldo_devedor3-parcela2)*(1+taxa)
parcela3=Saldo_devedor3/6

print('Saldo devedor 3: ',round(Saldo_devedor3,2))
print('Parcela: ',round(parcela3, 2),'     Juros: ', round((J1/6), 2))
print('Saldo devedor 4: ',round(Saldo_devedor4,2))
print('=============================================')

Saldo_devedor5=(Saldo_devedor4-parcela3)*(1+taxa)
parcela4=Saldo_devedor4/5

print('Saldo devedor 4: ',round(Saldo_devedor4,2))
print('Parcela: ',round(parcela4, 2),'     Juros: ', round((J1/5), 2))
print('Saldo devedor 5: ',round(Saldo_devedor5,2))
print('=============================================')

Saldo_devedor6=(Saldo_devedor5-parcela4)*(1+taxa)
parcela5=Saldo_devedor5/4

print('Saldo devedor 5: ',round(Saldo_devedor5,2))
print('Parcela: ',round(parcela5, 2),'     Juros: ', round((J1/4), 2))
print('Saldo devedor 6: ',round(Saldo_devedor6,2))
print('=============================================')

Saldo_devedor7=(Saldo_devedor6-parcela5)*(1+taxa)
parcela6=Saldo_devedor6/3

print('Saldo devedor 6: ',round(Saldo_devedor6,2))
print('Parcela: ',round(parcela6, 2),'     Juros: ', round((J1/3), 2))
print('Saldo devedor 7: ',round(Saldo_devedor7,2))
print('=============================================')

Saldo_devedor8=(Saldo_devedor7-parcela5)*(1+taxa)
parcela7=Saldo_devedor7/2

print('Saldo devedor 7: ',round(Saldo_devedor7,2))
print('Parcela: ',round(parcela7, 2),'     Juros: ', round((J1/2), 2))
print('Saldo devedor 8: ',round(Saldo_devedor8,2))
print('=============================================')

Saldo_devedor9=(Saldo_devedor8-parcela6)*(1+taxa)
parcela8=Saldo_devedor8/1

print('Saldo devedor 8: ',round(Saldo_devedor8,2))
print('Parcela: ',round(parcela8, 2),'     Juros: ', round((J1/1), 2))
print('Saldo devedor 9: ',round(0,2))
print('=============================================')
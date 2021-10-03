import os

taxa=0.0
divisao=0
principal=0
carencia=0

def coletaDados():
    global divisao, principal, carencia,taxa
    os.system('cls')
    print('\nSIMULADOR PRONAF +ALIMENTOSs\n')
    print('\n')
    principal=input('Qual o valor? ').replace(',','.')
    print('\n')
    divisao=input('Pagamento em quantas parcelas anuais? ')
    print('\n')
    carencia=input('Quantos anos de carência? ').replace(',','.')
    print('\n')
    taxa=input('Qual a taxa de juro? ').replace(',','.')
    print('\n')
    os.system('cls')
    try:
        principal=float(principal)
        divisao=int(divisao)
        carencia=int(carencia)
        taxa=(float(taxa))/100
        print('\nSIMULADOR PRONAF +ALIMENTOSs\n')
        print('\n')
        print(f'Valor: {principal:.2f}')
        print('Dividido em:',divisao, 'ano(s)')
        print('Carência:', carencia, 'ano(s)')
        print('Taxa de juros a.a:', round((taxa*100),2))
        print('\n')
        confirmacao=input("Digite S para simular     ")
        if confirmacao.upper()=='S':
            simulacao()
    except:
        print('\nSIMULADOR PRONAF +ALIMENTOSs\n')
        input('Verifique os dados digitados ')
        coletaDados()

def simulacao():
    n=divisao
    contador_parcela=1

    saldo_devedor=principal*(1+taxa)**(carencia+1)
    parcela=saldo_devedor/divisao
    os.system('cls')
    print('========RESUMO========')
    print(f'Valor: {principal:.2f}')
    print('Dividido em:',divisao, 'ano(s)')
    print('Carência:', carencia, 'ano(s)')
    print('Taxa de juros a.a:', round((taxa*100),2))
    print('\n')

    print('==================================================')
    print(f'Parcela {contador_parcela} = R$ {parcela:.2f}\n')
    print('==================================================')
    while n > 0:
        n=n-1
        saldo_devedor=saldo_devedor-parcela
        saldo_devedor=saldo_devedor*(1+taxa)
        if n>0:
            parcela=saldo_devedor/n
            contador_parcela+=1
        else:
            break   
        print(f'Parcela {contador_parcela} = R$ {parcela:.2f}\n')
        print('==================================================')

coletaDados()
print('\n')
novaSimulacao=input('Fazer nova simulacao? S para Sim e N para Não: ')
if novaSimulacao.upper()=='S':
    coletaDados()
else:
    print('\nFIM DO PROGRAMA')

    
    


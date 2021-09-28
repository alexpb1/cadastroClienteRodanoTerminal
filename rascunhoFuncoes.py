import sqlite3
import os
lista=[]
encontrado=[]
n1=0
n2=0
i=j=100
opcao=''
contador=0

def cabecario():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[34m','\n=============== CADASTRO DE CLIENTES ==================\n')

def menu():
    global opcao
    cabecario()
    print('\n 1 - Buscar Cliente')
    print(' 2 - Cadastrar Cliente')
    print(' 3 - Editar Cliente')
    print(' 4 - Deletar Cliente \n')
    opcao=input("Digite a opção desejada: ")
    if opcao=='1':
        cabecario()
        buscar=input('Digite dados do cliente para buscar: ')
        buscar_cliente(buscar)
        menu()
    if opcao=='2':
        cabecario()
        cadastrar_cliente()
        menu()
    if opcao =='3':
        menu()
    if opcao =='4':
        menu()
    

def cadastrar_cliente():
    global caminho, c
    nome=input("Nome do cliente: ")
    endereco=input("Endereço: ")
    fone=input("Telefone: ")
    email=input("Endereço de email: ")
    caminho="D:\\DB\\dbTeste.db"
    conexao=sqlite3.connect(caminho)
    c=conexao.cursor()
    c.execute("""
    INSERT INTO tb_clientes (NOME, ENDERECO, FONE, EMAIL)
    VALUES (?, ?, ?, ?)
    """,(nome, endereco, fone, email))
    conexao.commit()
    conexao.close()
    print('\033[34m',)
    input('\nCliente cadastrado. Tecle enter para voltar ao Menu...')


def buscar_cliente(objeto):
    global n1, n2,lista,encontrado
    caminho="D:\\DB\\dbTeste.db"
    conexao=sqlite3.connect(caminho) 
    c=conexao.cursor()
    c.execute("""
    SELECT * FROM tb_clientes;
    """)
    for linha1 in c.fetchall():
        linha=list(linha1)
        del linha[0]
        lista.append(linha)
    if objeto!="":
        for line in lista:  
            for coluna in line:
                if coluna==objeto:
                    encontrado.append(lista[n2])
                if n1<len(lista[0]):
                    n1+=1
                if n1==len(lista[0]):
                    n1=0 
            n2+=1
        n2=0
    else:
        buscar_cliente()
    if len(encontrado)==1:
        print('\033[31m','\n Nome: ', encontrado[0][0])
        print('\n Endereço: ', encontrado[0][1])
        print('\n Telefone: ', encontrado[0][2])
        print('\n Email: ', encontrado[0][3])
        print('\033[34m')
        input('\nTecle enter para retornar ao menu... \n')
    if len(encontrado)>1:
        contador=1
        print('\nEncontramos os seguintes clientes: \n')
        for pessoa in encontrado:
            print (contador, ' - ',pessoa)
            contador+=1
        cliente_select=int(input('\nDigite o número referente a um cliente: \n'))-1
        cabecario()
        print('\033[31m','\n Nome: ', encontrado[cliente_select][0])
        print('\n Endereço: ', encontrado[cliente_select][1])
        print('\n Telefone: ', encontrado[cliente_select][2])
        print('\n Email: ', encontrado[cliente_select][3])
        print('\033[34m')
        input('\nTecle enter para retornar ao menu... \n')
    if len(encontrado) ==0:
        print('\033[31m','\n Nenhum cliente localizado.')
        print('\033[34m')
        input('\nTecle enter para retornar ao menu... \n')
    conexao.close()
    lista.clear()
    encontrado.clear()




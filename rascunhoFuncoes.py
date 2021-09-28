import sqlite3
import os
lista=[]
n1=0
n2=0
i=j=100
opcao=''

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
    if opcao not in ('1','2','3','4'):
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
    global n1, n2, i, j, lista
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
                    i=n2
                    j=n1
                if n1<len(lista[0]):
                    n1+=1
                if n1==len(lista[0]):
                    n1=0 
            n2+=1
        n2=0
    else:
        buscar_cliente()

    if i!=100 and j!=100:
        print('\033[31m','\n Nome: ', lista[i][0])
        print('\n Endereço: ', lista[i][1])
        print('\n Telefone: ', lista[i][2])
        print('\n Email: ', lista[i][3])
        print('\033[34m')
        input('\nTecle enter para retornar ao menu... \n')
    else:
        print('\033[31m','\n Nenhum cliente localizado.')
        print('\033[34m')
        input('\nTecle enter para retornar ao menu... \n')
    i=j=100
    conexao.close()
    lista.clear()




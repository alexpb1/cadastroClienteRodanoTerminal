import sqlite3
from sqlite3 import Error
import os
lista=[]
n1=0
n2=0
n3=0
encontrado=''
cont_lista=0

def cabecario():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('=============== CADASTRO DE CLIENTES ==================\n')

def menu():
    global opcao
    print('\n 1 - Buscar Cliente')
    print(' 2 - Cadastrar Cliente')
    print(' 3 - Editar Cliente')
    print(' 4 - Deletar Cliente \n')
    opcao=input("Digite a opção desejada: ")
    if opcao=='2':
        cabecario()
        cadastrar_cliente()
    if opcao=='1':
        cabecario()
        buscar_cliente()
    if opcao not in ('1','2','3','4'):
        cabecario()
        menu()


def cadastrar_cliente():
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
    input('\nCliente cadastrado. Tecle enter para voltar ao Menu...')
    cabecario()
    menu()

def buscar_cliente():
    global encontrado, n1, n2, n3, lista, lista1, cont_lista
    caminho="D:\\DB\\dbTeste.db"
    conexao=sqlite3.connect(caminho) 
    c=conexao.cursor()
    c.execute("""
    SELECT * FROM tb_clientes;
    """)
    #resovler esse problema nesse ponto, precisa incluir na lista apenas elemento que sejam str.
    for linha in c.fetchall():
        if type(linha)==str:
            lista=lista+list(linha)
    print(lista)

    busca=input('\nBusque por Nome ou Endereço completo ou Telefone ou email: ')
    for line in lista:  
        for coluna in line:
            if coluna==busca:
                if encontrado!="":
                    encontrado=encontrado+", "+busca
                    print(n2, n1)   
                else:
                    encontrado=encontrado+busca
                    print(n2, n1)
            if n1<len(lista[0]):
                n1+=1
            if n1==len(lista[0]):
                n1=0
        n2+=1
    print('')
    lista==[]
    input('\nCliente localizado, tecle enter para retornar ao menu... \n')
    conexao.close()
    cabecario()
    menu()

cabecario()
menu()




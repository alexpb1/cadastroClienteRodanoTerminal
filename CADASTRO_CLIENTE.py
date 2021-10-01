import sqlite3
import os
lista=[]
encontrado=[]
n1=n2=0
i=j=100
opcao=''
contador=0
cliente_selecionado=0
cliente_select=0

def cabecario():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[34m','\n=============== CADASTRO DE CLIENTES ==================\n')

def menu():
    global opcao
    opcao=0
    cabecario()
    print('\n 1 - Buscar Cliente')
    print('\n 2 - Cadastrar Cliente')
    print('\n 3 - Editar Cliente')
    print('\n 4 - Deletar Cliente \n')
    print('\n')
    opcao=input("Digite a opção desejada: ")

    if opcao=='1':
        cabecario()
        buscar_cliente()
        exibir_busca()
        input('\nTecle enter para voltar ao Menu. ')
        menu()
    if opcao=='2':
        cabecario()
        cadastrar_cliente()
        menu()  
    if opcao =='3':
        cabecario()
        buscar_cliente()
        exibir_busca()
        if cliente_selecionado!=-1:
            escolha=input('Quer mesmo editar? ')
            if escolha =='s':
                editar_cliente()
        menu()
    if opcao =='4':
        cabecario()
        buscar_cliente()
        exibir_busca()
        if cliente_selecionado!=-1:
            escolha=input('Digite S para deletar? ')
            if escolha =='s':
                deletar_cliente()
        menu()

def cadastrar_cliente():
    global caminho, c
    nome=input("Nome do cliente: ")
    endereco=input("Endereço: ")
    fone=input("Telefone: ")
    email=input("Endereço de email: ")
    print('\n')
    confirmacao=input('Digite S para gravar o cliente. ')
    if confirmacao.upper()=='S':
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

def buscar_cliente():
    global n1, n2,lista,encontrado
    lista.clear()
    encontrado.clear()
    caminho="D:\\DB\\dbTeste.db"
    conexao=sqlite3.connect(caminho) 
    c=conexao.cursor()
    c.execute("""
    SELECT * FROM tb_clientes;
    """)
    for linha1 in c.fetchall():
        linha=list(linha1)
        lista.append(linha)
    conexao.close()
    buscar=input('Digite dados do cliente para buscar: ')
    if buscar!="":
        for line in lista:  
            for coluna in line:
                if coluna==buscar:
                    encontrado.append(lista[n2])
                if n1<len(lista[0]):
                    n1+=1
                if n1==len(lista[0]):
                    n1=0 
            n2+=1
        n2=0
    
def exibir_busca():   
    global cliente_selecionado, cliente_select
    cliente_selecionado=-1
    if len(encontrado)==1:
        cliente_selecionado=encontrado[0][0]
        print('\033[31m','\n Nome: ', encontrado[0][1])
        print('\n Endereço: ', encontrado[0][2])
        print('\n Telefone: ', encontrado[0][3])
        print('\n Email: ', encontrado[0][4])
        print('\033[34m')
    if len(encontrado)>1:
        contador=1
        print('\nEncontramos os seguintes clientes: \n')
        for pessoa in encontrado:
            print (contador, ' - ',pessoa)
            contador+=1
        cliente_select=int(input('\nDigite o número referente a um cliente: '))-1
        if cliente_select >= 0 and cliente_select<len(encontrado):
            cliente_selecionado=encontrado[cliente_select][0]
            cabecario()
            print('\033[31m','\n Nome: ', encontrado[cliente_select][1])
            print('\n Endereço: ', encontrado[cliente_select][2])
            print('\n Telefone: ', encontrado[cliente_select][3])
            print('\n Email: ', encontrado[cliente_select][4])
            print('\033[34m')
        
    if len(encontrado) ==0:
        print('\033[31m','\n Nenhum cliente localizado.')
        print('\033[34m')

def deletar_cliente():
    global cliente_selecionado
    print('função de deletar sendo executado')
    caminho="D:\\DB\\dbTeste.db"
    conexao=sqlite3.connect(caminho)
    c=conexao.cursor()
    c.execute("DELETE FROM tb_clientes WHERE N_ID_CLIENTE=?", (cliente_selecionado,))
    conexao.commit()
    conexao.close()

def editar_cliente():
    global cliente_selecionado, cliente_select
    cabecario()
    print('\nNome atual: ', encontrado[cliente_select][1])
    NovoNome=input('Novo nome: ')
    print('\nEndereço atual: ', encontrado[cliente_select][2])
    NovoEndereco=input('Novo Endereço: ')
    print('\nTelefone atual: ', encontrado[cliente_select][3])
    NovoTelefone=input('Novo telefone: ')
    print('\nEmail atual: ', encontrado[cliente_select][4])
    NovoEmail=input('Novo Email: ')
    print('\n')
    confirmacao=input('Digite S para gravar as mudanças no cliente. ')
    caminho="D:\\DB\\dbTeste.db"
    conexao=sqlite3.connect(caminho)
    c=conexao.cursor()
    c.execute("UPDATE tb_clientes SET nome =?, endereco=?, fone=?, email=? WHERE N_ID_CLIENTE = ?",(NovoNome, NovoEndereco, NovoTelefone, NovoEmail, cliente_selecionado))
    conexao.commit()
    conexao.close()

cabecario()
menu()
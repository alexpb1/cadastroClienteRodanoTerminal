import sqlite3
from sqlite3 import Error

vsql=None

def inserir():
    caminho="D:\\DB\\dbTeste.db"
    conexao=sqlite3.connect(caminho) 
    conexao.execute("")
    conexao.commit()
    print('Registro inserido')
    conexao.close()
inserir()











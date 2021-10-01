import sqlite3
cliente_a_deletar=input('digite número do cliente à deletar. ')

def deletar_cliente():
    caminho="D:\\DB\\dbTeste.db"
    conexao=sqlite3.connect(caminho)
    c=conexao.cursor()
    c.execute("DELETE FROM tb_clientes WHERE N_ID_CLIENTE=?", (cliente_a_deletar,))
    conexao.commit()
    conexao.close()
  
deletar_cliente()

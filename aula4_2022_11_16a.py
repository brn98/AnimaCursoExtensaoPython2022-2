#1- passo: importar a biblioteca do banco de dados
import sqlite3

#2- passo: estabelecendo uma conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3- passo: criando um objeto do tipo cursor
cursor = conexao.cursor()

def imprimir():
  #4- passo: comando sql do banco
  sql = "SELECT  pessoa_id, nome, nome_civil, tipo FROM pessoas"
  
  #5- passo: executando o cursor "SQL" no SQLite
  cursor.execute(sql)
  
  #6- passo: exibindo consulta do banco de dados
  pessoas = cursor.fetchall()
  for pessoa in pessoas:
    print(pessoa)
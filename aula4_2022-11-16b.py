import sqlite3
conexao = sqlite3.connect("dc_universe.db")
cursor = conexao.cursor()

#comando para inserir no banco de dados
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

#executar o comando
cursor.execute(sql)

#confirmando ação de inserir e fechar o banco
conexao.commit()
conexao.close()
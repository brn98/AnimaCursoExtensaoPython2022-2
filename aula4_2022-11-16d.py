import aula4_2022_11_16c as bd
import aula4_2022_11_16a as imprimir

con, cur = bd.conectar()

nome = input("Informe o nome do herói/vilão:\n")
nome_civil = input("\nInforme a identidade secreta:\n")
tipo_numerico = input("\nTecle 1 para Herói(na) ou 2 para Vilã(o)")

print("\n\n")

sql = "SELECT MAX (pessoa_id)+1 FROM pessoas"
cur.execute(sql)
pessoa_id = cur.fetchone()[0]

if tipo_numerico == "1":
  tipo = "Herói(na)"
else:
  tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cur.execute(sql)
con.commit()
con.close()

imprimir = imprimir.imprimir()
#criando funções

preco = 1999.90

#calcular 5% de imposto, guardar na variavel e exibir

imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#criar uma função calcular_imposto() que cacula um imposto de 5% e retorna a quem pediu
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

#aqui é o uso da função, calculando e exibir na tela
preco = 1000
imposto = calcular_imposto(preco)
print(imposto)

#agora calcular imposto a aliquota agora é 7%
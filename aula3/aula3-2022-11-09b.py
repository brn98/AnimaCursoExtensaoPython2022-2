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
print(imposto,'\n\n')

#agora calcular imposto a aliquota agora é 7%

valores = [1.99, 24.50, 78.27, 1515.5]
#Calculando o imposto deste quatro valores e exibindo
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")

#declarando uma função com dois valores, caso o valor do juros não seja informada, defina 7% como padrão
def calcular_imposto_aliquota(valor, aliquota=7):
  imposto = valor * aliquota / 100
  return imposto
print("\n\n\n")
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}")
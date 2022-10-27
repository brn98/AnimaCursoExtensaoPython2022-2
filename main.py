#Comando input(): quero permitir que 
#O usuário digite algo...

nome = input("Qual o seu nome? ")
idade = int(input("Agora informe sua idade: "))
gen = input("E o seu gênero M ou F?")

#Comando de saída...

print("Seu nome é {} e você tem {} anos!\n".format(nome,idade))

#Mostrando o dobro da idade e ano de nascimento
ano = 2022
dobro = idade*2
nascimento = ano-idade
print("O dobro da sua idade é {}, seu ano de nascimento é {}!\n".format(dobro,nascimento))

#Estruturas condicionais
#E se eu quiser perguntar o gênero (M = Masculino e F = Feminino)
#Mostre (... E você também precisa/precisou prestar o serviço militar obrigatório)

if (idade>=18): 
  print("Vocês é maior de idade, ótimo! Já pode beber ou dirigir.")
  if (gen == 'M'): print("E você também precisa/precisou prestar o serviço militar obrigatório!")
else: 
  menorIdade=18-idade
  print(f"Vocês é menor de idade, que pena! Falta {menorIdade} anos pra você poder beber ou dirigir\n")



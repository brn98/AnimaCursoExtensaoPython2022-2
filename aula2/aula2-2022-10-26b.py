#Pede o nome e a nota do aluno (O a 10) e, se ele tirou nota 10, mostra ("Se é o bichão memo...")
nome=input("Informe seu nome: ")
nota=float(input("Digite sua nota: "))

if (nota == 10): 
  print(f"{nome}, se é o bichão memo hein...")
elif (nota >= 6 and nota <10):
  print(f"{nome}, você está dentro da média, mas não é o bichão ainda!")
else:
  print("Ai que buro, da zero pra ele!")
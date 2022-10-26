#Comando input(): quero permitir que 
#O usuário digite algo...

nome = input("Digite seu nome: ")
idade = int(input("Agora informe sua idade: "))

#Comando de saída...

print("Seu nome é {} e você tem {} anos!".format(nome,idade))

#Mostrando o dobro da idade e ano de nascimento
ano = 2022
dobro = idade*2
nascimento = ano-idade
print("O dobro da sua idade é {}, seu ano de nascimento é {}".format(dobro,nascimento))
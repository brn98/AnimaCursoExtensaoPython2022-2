print("Início da aula 3 (09/11/2022)\n")

contador = 1
i = 0

while(contador <= 5):
  print(contador)  
  contador += 1


#Laço for em python = for each
fruta = 'morango'
print(fruta,'\n')

#lista
frutas = ['morango', 'laranja', 'pêra']

#exibindo apenas a terceira fruta
print(frutas[2],'\n')

#quantas frutas eu tenho
print(len(frutas),'\n')

#Quero adicionar uma nova fruta
frutas.append('manga')
print(len(frutas),'\n')

#exemplo com while
while(i<=3):
  print(frutas[i])
  i += 1
else: i = 0
  
for i in frutas:
  print(frutas[i])
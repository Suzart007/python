import os
os.system("cls")
#           0   1   2   3   4   5   6   7   8   9   <== indices positivos
lista = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#           -10 -9  -8  -7  -6  -5  -4  -3  -2  -1  <== indices negativos

print(lista)
print(lista[4])
print(lista[0], lista[9])
print(lista[0], lista[-7])


#Slacing - fatiamento de lista


#           0   1   2   3   4   5   6   7   8   9   <== indices positivos
lista = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#           -10 -9  -8  -7  -6  -5  -4  -3  -2  -1  <== indices negativos

nova_lista = lista[2: 8]
print(lista)
print(nova_lista)

#Sintaxe: lista [inicio, fim -1, passo]


print(lista[4:])
print(lista[: 5])
print(lista[:], lista)
os.system("cls")
print(lista[0: 10: 3])
print(lista[-8:-1:2])
print(lista)
print(lista)


os.system("cls")
#Slicing de strings

frase = "Meu Deus! não acredito que isso tambem funciona com string"
print(frase)
print(frase)

os.system("cls")
l = "python"
l = "J" = l[1:]
print(l)
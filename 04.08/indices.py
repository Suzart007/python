import os
os.system("clear")

#        0.  1.  2.  3.  4.  5.  6. <- indices positivos
lista = [0, 10, 20, 30, 40, 50, 60, 70]
#       -8  -7. -6. -5. -4. -3. -2. -1  <- indices negativos

print(lista)
print(lista[2])
print(lista[-5])

# Exibir o primeiro e ultimo elemento
print("Primeiro:",lista[0], "\nUltimo:", lista[-1])

# slicing - Fatiamento (lista e string)
#        0.  1.  2.  3.  4.  5.  6. <- indices positivos
lista = [0, 10, 20, 30, 40, 50, 60, 70]
#       -8  -7. -6. -5. -4. -3. -2. -1  <- indices negativos

# slicing: lista[inicio: fim - 1: passo]
os.system("clear")
print(lista[2: 5])
sub_lista = lista[1:4]
print (lista,sub_lista)
print(lista[-6:-2])
print(lista[4: ])
print(lista[ :5])
print(lista[::-1])

os.system("clear")
# fatiando strings
#        01234567890123456789012345678901234567890123456
frase = "Nao acredito que tudo isso funciona aqui também"
print(frase)
print(frase[15])
print(frase[10:20])
print(frase[-1])
print(frase[-20:-10])
print(frase[5:35:2])
print(frase[:30:3])
print(frase[::5])


 
import os


# inicializando uma lista com valores
os.system("clear")
lista = [22, "Fiap", True, 3.3, "Edson"]

print(lista)

for elem in lista:
    print(elem)

# Métodos (e afins) de manipulação de listas
# list() ou [] - cria uma lista vazia
os.system("clear")
lista = [] #list()
print(lista)

# append(elemento) - insere um elemento no final da lista
os.system("clear")
lista = [] #list()
print(lista)
lista.append("Edson")
print(lista)
lista.append(33)
print(lista)
elem = "Fiap"
lista.append(elem)
print(lista)
# elem = input("Elemento: ")
lista.append(elem)
print(lista)

# insert(indice, elemento) - insere um elemento em uma posicao da lista
os.system("clear")
#          0      1     2        3
lista = ['Edson', 33, 'Fiap', 'Novidade']
print(lista) 
lista.insert(1, 56.7)
print(lista)
lista.insert(25, 56.7)
print(lista)

# pop(<indice>) - remove um (ou o ultimo) elemento pelo indice
os.system("clear")
#          0      1     2        3
lista = ['Edson', 33, 'Fiap', 'Novidade']
print(lista) 
lista.pop()
print(lista) 
elem = lista.pop(0) # o índice deve existir, senao ocorre uma falha
print(lista) 
print(elem)

# remove(conteudo) - remove um elemento pelo conteudo
os.system("clear")
#          0      1     2        3
lista = ['Edson', 33, 'Fiap', 'Novidade']
print(lista) 
lista.remove('Edson') # o elemento deve existr para ser removido
print(lista)

# index(elemento) - retorna o indice onde o elemento está
os.system("clear")
#          0      1     2        3
lista = ['Edson', 33, 'Fiap', 'Novidade']
print(lista) 
indice = lista.index("Edson") # o elemento deve existir para o índice ser retornado
print(indice)

# count(elemento) - conta quantos elementos especificos há na lista
os.system("clear")
lista = ['Edson', 33, 'Fiap', 'Novidade', 33, 33]
print(lista) 
elem = "João"
qtd = lista.count(elem)
print(f"Há {qtd} elementos {elem} na lista")

# aplicação do count()
os.system("clear")
lista = ['Edson', 33, 'Fiap', 'Novidade', 33, 33]

elem = 56
qtd = lista.count(elem)

if qtd == 0: # não há o elemento na lista
    print(f"O elemento '{elem}' não está na lista")
else:
    indice = lista.index(elem) # o elemento deve existir para o índice ser retornado
    print(f"O elemento {elem} está no indice {indice}")

# Fazer um programa que inicialize uma lista vazia.
# Peça para o usuário digitar elementos até que seja digitado '.''
# Exibir o conteudo da lista
'''
# v2.0 - Depois de mostrar a lista, colocar em uma lista somente os dados inteiros e na outra os 
# demais dados
# ['Edson', '33', '23', '21', '95', 'oi', 'maria', 'Ester', 'Ana', 'Ouro', 'Nicola', 'Bronze']
# lista inteiros = [33, 23, 21, 95]
# lista outros = ['Edson', 'oi', 'maria', 'Ester', 'Ana', 'Ouro', 'Nicola', 'Bronze']
'''
"""
Digite elementos:
34
67
Edson
True
.
lista = [34, 67, 'Edson', True]
"""# Fazer um programa que inicialize uma lista vazia.
# Peça para o usuário digitar elementos até que seja digitado '.''
# Exibir o conteudo da lista
'''
# v2.0 - Depois de mostrar a lista, colocar em uma lista somente os dados inteiros e na outra os 
# demais dados
# ['Edson', '33', '23', '21', '95', 'oi', 'maria', 'Ester', 'Ana', 'Ouro', 'Nicola', 'Bronze']
# lista inteiros = [33, 23, 21, 95]
# lista outros = ['Edson', 'oi', 'maria', 'Ester', 'Ana', 'Ouro', 'Nicola', 'Bronze']
'''
"""
Digite elementos:
34
67
Edson
True
.
lista = [34, 67, 'Edson', True]
"""
os.system("clear")
lista = list()
print("Digite elementos:")
while True:
    elem = input()
    if elem == '.': #se digitou ponto
        break # sai
    else: # não digitou ponto
        lista.append(elem)

print(lista)
 
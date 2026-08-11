import os
os.system("clear")

# Métodos para listas
# list() ou []- cria uma lista vazia
lista = [] # list()
print(lista)

# append(elemento) - insere um elemento no final da lista
lista.append("Edson")
lista.append("Martelo")
lista.append(45)
elem = 45.66
lista.append(elem)
#elem = input("Elemento: ")
#lista.append(elem)
print(lista)

# insert(posicao, elemento) - insere um elemento em uma posicao da lista
lista.insert(1, "Novo")
lista.insert(10, "e agora?")
print(lista)

# pop([indice]) - remove o ultimo elemnto ou o indice especificado
os.system("clear")
lista = ['Edson', 'Novo', 'Martelo', 45, 45.66, 'e agora?']
print(lista)
lista.pop()
print(lista)
elem = lista.pop(2) # cuidado, o índice deve existir
print(lista, elem)

# remove(elemento) - remove pelo elemento
os.system("clear")
lista = ['Edson', 'Novo', 'Martelo', 45, 45.66, 'e agora?']
print(lista)
lista.remove("Edson") # cuidado, o elemento deve existir na lista
print(lista)

# index(elemento) - retorna o indice
os.system("clear")
lista = ['Edson', 'Novo', 'Martelo', 45, 45.66, 'e agora?']
print(lista)
indice = lista.index("Edson") # cuidado, o elmento deve existir
print(f"Índice = {indice}")

# count() - conta quantos elementos específicos exite na lista
os.system("clear")
lista = ['Edson', 'Novo', 'Martelo', 45, 45.66, 'e agora?', 45, 45]
qtd = lista.count("Joao")
print("Quantidade: ", qtd)

# exemplo:
os.system("clear")
lista = ['Edson', 'Novo', 'Martelo', 45, 45.66, 'e agora?', 45, 45]
elem = "Joao"
if lista.count(elem) == 0: # o elemento nao existe
    print(f"O elemento '{elem}'não existe na lista!" )
else:
    indice = lista.index(elem)
    print(f"O elemento '{elem}' está no índice {indice}")

# len(objeto) - conta quantos elemento existem na lista (ou em uma string)
os.system("clear")
lista = ['Edson', 'Novo', 'Martelo', 45, 45.66, 'e agora?', 45, 45]
qtd = len(lista)
print(qtd)
qtd = len("Edson de Oliveira")
print(qtd)

# sum(lista_numeros) - soma o conteudo da lista (*nutela)
os.system("clear")
lista = [345, 45, -56, 56.87, 3.343]
somatoria = sum(lista)
print("Soma = ", somatoria)

somatoria = 0

for elem in lista:
    somatoria = somatoria + elem

print("Soma = ", somatoria)

# + - concatenação (junçao)
os.system("clear")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(f"Lista1 = {lista1}")
print(f"Lista2 = {lista2}")
print(f"Lista3 = {lista3}")

# extend(lista) - insere uma lista no final da outra
os.system("clear")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(f"Lista1 = {lista1}")
print(f"Lista2 = {lista2}")

# copy()
os.system("clear")
lista1 = [1, 2, 3]
lista2 = lista1.copy()
lista1.append(4)
print(f"Lista1 = {lista1}")
print(f"Lista2 = {lista2}")

# sort() - ordena uma lista numerica
os.system("clear")
lista = [45, 3, 44, 76, 12, 34]
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True) # ordem decrescente
print(lista)

# reverse() - inerte a ordem da lista
os.system("clear")
lista = [45, 3, 44, 76, 12, 34]
print(lista)
lista.reverse()
print(lista)

# clear() - apaga todos os elemntos da lista
os.system("clear")
lista = [45, 3, 44, 76, 12, 34]
print(lista)
lista.clear()
print(lista)

# del objeto - exclui do programa a variavel / elemento
os.system("clear")
lista = [45, 3, 44, 76, 12, 34]
print(lista)
del lista
print(lista)
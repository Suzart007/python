# SET() - CONJUNTOS 
'''
CARACTERÍSTICAS:
- ARMAZENA ITENS NÃO DUpLICADOS
- SUPORTA OPERAÇÕES ARITMÉTICAS DE CONJUNTOS
- NÃO É POSSÍVEL INTERAR COM OS ELEMENTOS
- SUPORTA ELEMENTOS DE QUAISQUER TIPO
- SAO ESCRITOS ENTRE CHAVES
'''

import os
os.system("cls")

# utilizando um conjuntos vazio
conjunto = set()
print(conjunto)
#          0. 1. 2  3 
numeros = [2, 3, 3, 6, 5, 7, 3, 2, 7, 10]
conjunto = set(numeros)
print(numeros)
print(conjunto)

lista = list(conjunto)
print(lista)
lista.pop()
print(lista)
conjunto = set(lista)
print(conjunto)

print(20 * '-')

# add() - Adiciona um elemento no conjunto
conjunto = {2, 3, 4, 5, 6, 7, 8}
print(conjunto)
conjunto.add(10)
print(conjunto)
print(20 * '-')

# remove() - remove um item do set (conjunto). Se nao existir, gera uma falha
conjunto = {2, 3, 4, 5, 6, 7, 8}
print(conjunto)
conjunto.remove(4)
print(conjunto)
print(20 * '-')

# discard() - remove um item do conjunto. Se nao existir, vida que segue
conjunto = {2, 3, 4, 5, 6, 7, 8}

'''
lista = [4, 5, 6]
dicionario = {'nome':'edson'  ,   'idade': 52}
conjunto = set()
'''

print(conjunto)
conjunto.discard(33)
print(conjunto)
print(20 * '-')

# clear() - apaga os elementos do conjunt
conjunto = {2, 3, 4, 5, 6, 7, 8}
print(conjunto)
conjunto.clear()
print(conjunto)
print(20 * '-')
# ================ OPERAÇÕES ARITMÉTICAS com conjuntos
# union() ou | - une os conjjuntos
a = {0, 1, 3, 5, 7, 9, 10}
b = {0, 2, 4, 6, 8, 10}
c = a.union(b)
print(a)
print(b)
print(c)
print(20 * '-')

a = {0, 1, 3, 5, 7, 9, 10}
b = {0, 2, 4, 6, 8, 10}
c = a | b
print(a)
print(b)
print(c)
print(20 * '-')

# intersection ou & - Efetua a intersecção entre dois conjuntos
a = {0, 1, 3, 5, 7, 9, 10}
b = {0, 2, 4, 6, 8, 10}
c = a.intersection(b) # ou c = a & b
print(a)
print(b)
print(c)
print(20 * '-')

# ========= COMPARAÇÃO ENTRE CONJUNTOS
# operador in - associação
planetas = {"mercurio", "venus", "terra", "marte"}
print("venus" in planetas)

planeta = "jupiter"
if planeta in planetas:
    print(f"{planeta} está em {planetas}")
else:
    print(f"{planeta} NÃO está em {planetas}")
print(20 * '-')

# operador == ou !=
planetas1 = {"terra", "venus", "mercurio", "marte"}
planetas2 = {"terra", "venus", "mercurio", "satur"}

print(planetas1 == planetas2)
print(planetas1 != planetas2)
print(20 * '-')

# operadores < e >
planetas1 = {"terra", "venus", "mercurio", "marte"}
planetas2 = {"terra", "venus", "mercurio", "marte", "lua"}
print(planetas1 > planetas2)
print(20 * '-')

# diference ou - -> a diferença entre dois conjuntos e um conjunto contendo os elementos
# da esquerda que não estão na direita
planetas1 = {"venus", "mercurio", "terra", "netuno", "marte"}
planetas2 = {"terra", "jupiter", "urano", "saturno", "marte"}
print(planetas2 - planetas1)
print(planetas1.difference(planetas2))
print(20 * '-')

# diferença simétrica - esquerda comparado com o da direita e vice-versa
# ^ ou symmetric_diference
planetas1 = {"venus", "mercurio", "terra", "netuno", "marte"}
planetas2 = {"terra", "jupiter", "urano", "saturno", "marte"}
print(planetas1 ^ planetas2)
print(20 * '-')

# disjuntos - NÃO possuem elementos em comum | isdisjoint
planetas1 = {"venus", "mercurio", "terra", "netuno", "marte"}
planetas2 = { "jupiter", "urano", "saturno"}
print(planetas1.isdisjoint(planetas2)) # NÃO tem elementos em comum?
print(20 * '-')

# |= - Faz a uniao em ordem aleatória
planetas1 = {"venus", "mercurio", "terra", "netuno", "marte"}
planetas2 = {"terra", "jupiter", "urano", "saturno", "marte"}
planetas1 |= planetas2
print(planetas1)
print(planetas2)
print(20 * '-')

# copy() - copiando conjuntos
planetas1 = {"venus", "mercurio", "terra", "netuno", "marte"}
planetas2 = planetas1.copy()
planetas2.add("lua")
print(planetas1)
print(planetas2)
print(20 * '-')

# pop() - remove um elemento aleatorio
planetas = {"venus", "mercurio", "terra", "netuno", "marte"}
print(planetas)
removido = planetas.pop()
print(planetas)
print("Removido: ", removido)

print(20 * '-')
# casting
#        0. 1. 2. 3. 4. 5
lista = [1, 1, 2, 3, 3, 3, 4, 5, 6, 6]
conjunto = set(lista)
print(lista)
print(conjunto)
print(20 * '-')
conjunto = {3, 6, 7, 8, 5, 4, 4, 4, 4}
print(conjunto)
lista = list(conjunto)
print(lista)
lista[0] = 10
print(lista)
conjunto = set(lista)
print(conjunto)

 
import os
os.system("clear")

# vetor
# - tem tamanho definido pelo programador
# - armazena dados do mesmo tipo
# - Para percorrer o vetor inteiro, use um laço

#         0   1   2   3   4
vetor = [45, 34, 23, 12, -5]

for indice in range(0, 5, 1):
    print(f"V[{indice}] = {vetor[indice]}")

for numero in vetor:
    print(numero)

for indice, numero in enumerate(vetor):
    print(f"V[{indice}] = {numero}")


soma = sum(vetor)
print("Soma =",soma)

soma = 0
for numero in vetor:
    soma += numero # soma = soma + numero
print("Soma =",soma)



#print(vetor[1])
#print(vetor)


 
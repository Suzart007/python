lista = []

for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    lista.append(num)

soma = 0
for num in lista:
    soma += num

media = soma / len(lista)

print("Média:", media)
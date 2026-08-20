lista = []

for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    lista.append(num)

maior = lista[0]

for num in lista:
    if num > maior:
        maior = num

print("Maior valor:", maior)
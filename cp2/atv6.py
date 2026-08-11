n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 < n2:
    inicio = n1
    fim = n2
else:
    inicio = n2
    fim = n1

for i in range(inicio, fim + 1):
    print(i)
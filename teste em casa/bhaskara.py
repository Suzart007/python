import os
os.system("cls")
import math

a = float(input("Digite o valor do A: "))
b = float(input("Digite o valor do B: "))
c = float(input("Digite o valor do C: "))


if a == 0:
    print("Não exite raiz")

delta = b**2 - 4 * a * c
if delta < 0:
    print("ERRO")

else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    print(f"o valor de x1 é igual a {x1:.1f} \ne do valor de x2 é {x2:.1f}")
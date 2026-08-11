import os
os.system("cls")


# Exercício.
# Dado um número, exibir o seu módulo matemático, ou seja,
# se for digitado um numero positivo, exibir o positivo e se
# for digitado um numero negativo, transforma-lo em positivo e exibir.


num = float(input("numero: "))

if num < 0:
    num = - num * -1

print(num)

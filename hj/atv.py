import os
os.system("cls")

salario = float(input("Digite o salário: R$ "))
bonus = 1000

ganho_final = salario + (salario * 0.06 if salario >= 10000 else salario * 0.04) + bonus

print("Ganho final:", ganho_final)
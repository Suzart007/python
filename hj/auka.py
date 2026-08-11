import os
os.system("cls")


# OPERADOR TERNÁRIO
# Ele substitui o comando de decisão composta (if else) em situações onde tenha apenas um comando
# no lado Treu e outro no lado False. Também serve como cálculo.

# Sintaxe:
# [variavel =] intrucao True if condicao else instrucao False

# Forma 1 - sem usar variável
'''
idade = 19
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

print("Maior de idade") if idade >= 18 else print("Menor de idade")
'''

# Forma 2 - usando variável e calculo - primário
# inss 10% -> mais de 5000 | até 5000 paga 5%
'''
salario = 1000

inss = salario * 0.1 if salario > 5000 else salario * 0.05

print(salario, inss)
'''

# Forma 3 - usando variável e calculo - secundário
# salario liq.= salario - inss 10% -> mais de 5000 | até 5000 paga 5% + bonus

salario = 1000
bonus = 500

sal_liq = salario - (salario * 0.1 if salario > 5000 else salario * 0.05) + bonus
# sal_liq = 10000   - 10% + 500
# sal_liq = 1000    - 5%  + 500

print(salario, sal_liq)
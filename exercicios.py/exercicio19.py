salario = float(input("Digite o seu salário, por favor: "))
if salario > 8157.41:
    salario_conta = 8157.41
else:
    salario_conta = salario

if salario_conta <= 1518.01:
    aliquota = 0.075
    deducao = 0
else:
    if salario_conta <= 2793.88:
        aliquota = 0.09
        deducao = 22.77
    else:
        if salario_conta <= 4190.83:
            aliquota = 0.12
            deducao = 106.59
        else:
            aliquota = 0.14
            deducao = 190.40


inss = salario_conta * aliquota - deducao
print(f"salario: {salario: .2f}")
print(f"INSS {inss: .2f}")              

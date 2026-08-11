import os
os.system("cls")

salario = float(input("Salário: R$ "))
if salario >= 0:
    salario_minimo = 1302
    qtd_falta = int(input("quantidade de faltas: "))


    if salario <= salario_minimo * 2:
        reajuste = salario * 0.0645


    elif salario <= salario_minimo * 5:
        reajuste = salario * 0.0455


    elif salario <= salario_minimo * 10:
        reajuste = salario * 0.0289


    elif salario <= salario_minimo * 15:
        reajuste = salario * 0.012


    else:
        reajuste = 0


    sal_reaj = salario + reajuste



    if qtd_falta == 0: 
        bonus = salario_minimo * 2


    elif qtd_falta <= 2: 
        bonus = salario_minimo 


    elif qtd_falta <= 5: 
        bonus = salario_minimo / 2

                
    else:
     bonus = 0


    ganho_total = sal_reaj + bonus


    print(f"""
    Relatorio:
    Salário: R$ {salario}
    Salário Reajustado: R$ {sal_reaj}
    Bônus: R$ {bonus}
    Ganho Total: R$ {ganho_total}
    """)
else:
    print("ERRO! Digite um salário positivo")
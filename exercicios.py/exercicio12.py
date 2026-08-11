salario = float(input("Digite seu sálario: "))
venda = float(input("Digite sua venda: "))

if venda > 100000 :
    bonus = salario * 2


else:
    bonus = salario * 1.5
    
print(f"Seu sálario é de: {salario}")
print(f"Seu venda é de: {venda}")
print(f"Seu bonus é de: {bonus}")
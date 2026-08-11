compra = float(input("Digite o valor gasto: "))
if compra > 5000:
    valor_final = compra * (1 - 0.075)
else:
    valor_final = compra * (1 - 0.035)
print(f"Valor gasto {compra: .2f}")
print(f"Valor com desconto {valor_final: .2f}")
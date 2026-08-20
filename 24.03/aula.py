print(True and False)
print(not(True or False and not True))

tempo = 7
debito = False
aposentado = False

if tempo >= 5 and not debito or aposentado:
    print("Tera isenção")

else:
    print("Não tera isenção")


# Exercício:
# A partir de uma compra, o usuário terá um desconto.
# - Se a compra for acima de 1000 reais, terá um desconto de 10%
# - Se a compra for entre (inclusive) 500 e 1000, terá um desconto de 5%
# - Se a compra for abaixo de 500, não terá desconto.
# Ao finalizar exiba: O valor da compra, o valor do desconto e o valor da compra
# com o desconto
 
compra = float(input("Digite o valor da compra: "))

if compra > 1000:
    desconto = compra * 0.10
elif compra >= 500:
    desconto = compra * 0.05
else:
    desconto = 0

valor_final = compra - desconto

print(f"Valor da compra: R$ {compra:.2f}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor final com desconto: R$ {valor_final:.2f}")
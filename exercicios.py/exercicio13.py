compra = float(input("Digite o valor da sua compra: "))

print("Digite o numero da sua forma de pagamento\n"
      "1 - PIX (desconto de 5%)\n"
      "2 - Dinheiro (O mesmo valor da compra)\n"
      "3 - Débito (Acréscimo de 1%)\n"
      "4 - Crédito (Acréscimo de 2,5%)")

pagamento = int(input())

if pagamento == 1 :
    reajuste = compra - (compra * 0.05)
else:
    if pagamento == 2 :
        reajuste = compra
    else:
        if pagamento == 3 :
            reajuste = compra + (compra * 0.01)
        else:
            if pagamento == 4 :
                reajuste = compra + (compra * 0.025)
            else:
                print("Forma de pagamento inválida!")
                reajuste = compra

print(f"Valor original: R${compra:.2f}\n"
      f"Valor ajustado: R${reajuste:.2f}")
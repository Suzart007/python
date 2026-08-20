import os
os.system("cls")

from estoque import *

estoque = {}

while True:
    print("1. Add")
    print("2. Entrada")
    print("3. Saída")
    print("4. Baixo")
    print("5. Total")
    print("0. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        adicionar_produto(estoque)

    elif opcao == "2":
        registrar_entrada(estoque)

    elif opcao == "3":
        registrar_saida(estoque)

    elif opcao == "4":
        estoque_baixo(estoque)

    elif opcao == "5":
        valor_total(estoque)

    elif opcao == "0":
        break
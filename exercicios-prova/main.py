import os
os.system("cls")

from contatos import *

agenda = {}

while True:
    print("1. Adicionar")
    print("2. Listar")
    print("3. Buscar")
    print("4. Editar")
    print("5. Remover")
    print("0. Sair")

    opcao = input("Opção: ").strip()

    if opcao == "1":
        adicionar_contato(agenda)

    elif opcao == "2":
        listar_contatos(agenda)

    elif opcao == "3":
        buscar_contato(agenda)

    elif opcao == "4":
        editar_telefone(agenda)

    elif opcao == "5":
        remover_contato(agenda)

    elif opcao == "0":
        break

    else:
        print("Inválido")
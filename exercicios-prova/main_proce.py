import os
os.system("cls")

from processador import *

texto = ""

while True:
    print("1. Contar")
    print("2. Substituir")
    print("3. Maiúsc")
    print("4. Minúsc")
    print("5. Sem dup")
    print("0. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        texto = input("Texto: ")

        contagem = contar_palavras(texto)

        for palavra, qtd in contagem.items():
            print(f"'{palavra}': {qtd}x")

    elif opcao == "2" and texto:
        subs = {"antigo": "novo"}
        texto = substituir_multiplas(texto, subs)

    elif opcao == "3" and texto:
        texto = texto.upper()
        print(texto)

    elif opcao == "4" and texto:
        texto = texto.lower()
        print(texto)

    elif opcao == "5" and texto:
        texto = remover_duplicadas(texto)
        print(texto)

    elif opcao == "0":
        break
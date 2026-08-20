from sub import *


while True:

    print()
    print("=== CENTRAL DE ANÁLISE DE TEXTOS E LISTAS ===")
    print("1 - Exibir o primeiro e último item de uma lista")
    print("2 - Inverter um texto")
    print("3 - Analisar e tratar uma frase")
    print("4 - Substituir palavra em uma frase")
    print("5 - Recortar uma lista por intervalo")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        entrada = input("Itens: ")
        lista = entrada.split(",")

        extremos = obter_extremos(lista)

        print("Primeiro..:", extremos[0])
        print("Último....:", extremos[1])

    elif opcao == "2":

        texto = input("Texto: ")

        resultado = inverter_texto(texto)

        print("Texto invertido:", resultado)

    elif opcao == "3":

        frase = input("Frase: ")

        resultado = analisar_frase(frase)

        print("Frase tratada.............:", resultado[0])
        print("Quantidade de caracteres..:", resultado[1])
        print("Quantidade de palavras....:", resultado[2])

    elif opcao == "4":

        frase = input("Frase: ")
        antiga = input("Palavra a substituir: ")
        nova = input("Nova palavra: ")

        resultado = substituir_palavra(frase, antiga, nova)

        print("Resultado:", resultado)

    elif opcao == "5":

        entrada = input("Itens: ")
        lista = entrada.split(",")

        inicio = int(input("Índice inicial: "))
        fim = int(input("Índice final: "))

        resultado = filtrar_intervalo(lista, inicio, fim)

        print("Fatia da lista:", resultado)

    elif opcao == "0":

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida.")
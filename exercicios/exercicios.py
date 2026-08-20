

def calcular_delta():
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    delta = b**2 - 4*a*c
    print("Delta =", delta)


def maior_2():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    
    if a > b:
        print("Maior:", a)
    else:
        print("Maior:", b)


def menor_3():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    c = float(input("Digite o terceiro número: "))
    
    if a <= b and a <= c:
        print("Menor:", a)
    elif b <= a and b <= c:
        print("Menor:", b)
    else:
        print("Menor:", c)


def ordem_crescente():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    
    if a < b:
        print("Ordem crescente:", a, b)
    else:
        print("Ordem crescente:", b, a)


def soma_lista():
    lista = []
    qtd = int(input("Quantos números deseja inserir? "))
    
    for i in range(qtd):
        num = float(input(f"Digite o {i+1}º número: "))
        lista.append(num)
    
    soma = 0
    for num in lista:
        soma += num
    
    print("Soma:", soma)


def media_lista():
    lista = []
    qtd = int(input("Quantos números deseja inserir? "))
    
    for i in range(qtd):
        num = float(input(f"Digite o {i+1}º número: "))
        lista.append(num)
    
    soma = 0
    for num in lista:
        soma += num
    
    media = soma / len(lista)
    print("Média:", media)


def maior_lista():
    lista = []
    qtd = int(input("Quantos números deseja inserir? "))
    
    for i in range(qtd):
        num = float(input(f"Digite o {i+1}º número: "))
        lista.append(num)
    
    maior = lista[0]
    
    for num in lista:
        if num > maior:
            maior = num
    
    print("Maior valor:", maior)




opcao = -1

while opcao != 0:
    print("\n===== MENU =====")
    print("1 - Calcular Delta")
    print("2 - Maior entre 2 números")
    print("3 - Menor entre 3 números")
    print("4 - Ordem crescente (2 números)")
    print("5 - Soma da lista")
    print("6 - Média da lista")
    print("7 - Maior da lista")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        calcular_delta()
    elif opcao == 2:
        maior_2()
    elif opcao == 3:
        menor_3()
    elif opcao == 4:
        ordem_crescente()
    elif opcao == 5:
        soma_lista()
    elif opcao == 6:
        media_lista()
    elif opcao == 7:
        maior_lista()
    elif opcao == 0:
        print("Encerrando...")
    else:
        print("Opção inválida!")
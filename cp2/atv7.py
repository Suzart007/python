n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
ordem = input("Digite C para crescente ou D para decrescente: ")

if ordem == "C" or ordem == "c":
    if n1 < n2:
        for i in range(n1, n2 + 1):
            print(i)
    else:
        for i in range(n2, n1 + 1):
            print(i)

elif ordem == "D" or ordem == "d":
    if n1 > n2:
        for i in range(n1, n2 - 1, -1):
            print(i)
    else:
        for i in range(n2, n1 - 1, -1):
            print(i)
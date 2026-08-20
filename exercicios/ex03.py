a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a <= b and a <= c:
    print("Menor:", a)
elif b <= a and b <= c:
    print("Menor:", b)
else:
    print("Menor:", c)
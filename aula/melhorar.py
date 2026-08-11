nota1 = float(input("Nota 1: "))

if nota1 >= 0 and nota1 <=10:
    nota2 = float(input("Nota 2: "))
    if nota2 >= 0 and nota2 <=10:
        # as duas notas são válidas
        media = (nota1 + nota2) / 2
        print(f"Media: {media}")
    else:
        print(f"Nota {nota2} é inválida")
else:
    print(f"Nota {nota1} é inválida")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
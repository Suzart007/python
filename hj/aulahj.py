# Revisão
import os
os.system("clear")
'''
# 1. Dada uma nota, verificar se ela é válida ou não

nota = float(input("Nota: ")) # 4
# if else com operador lógico and
if nota >= 0 and nota <= 10:
    print("Válida") # Bloco True
else:
    print("Inválida") # Bloco False


# if encadeado sem operador lógico
if nota >= 0:
    if nota <= 10:
        print("Valida!")
    else: # nota > 10
        print("Inválida")
else: # nota < 0 
    print("Valida")


# 2. Dadas 3 notas, exibir a de menor valor
import os
os.system("clear")
nota1 = float(input("Nota 1: ")) # 5
nota2 = float(input("Nota 2: ")) # 3
nota3 = float(input("Nota 3: ")) # 7

menor = nota1 

if nota2 < menor:
    menor = nota2 # menor -> 3

if nota3 < menor:
    menor = nota3

print(menor)

código estagiário -> junior
if nota1 < nota2 and nota1 < nota3:
    menor = nota1
elif nota2 < nota1 and nota2 < nota3:
    menor = nota2
elif nota3 < nota1 and nota3 < nota2:
    menor = nota3
'''

# 3. Dadas 3 notas, calcular a media da CP. 
# As notas devem ser válidas, senão encerra o programa. v2
import os
os.system("cls")
nota1 = float(input("Nota 1: ")) # 5
if nota1 >= 0 and nota1 <= 10: # condicao para nota válida
    nota2 = float(input("Nota 2: ")) # 3
    if nota2 >= 0 and nota2 <= 10:
        nota3 = float(input("Nota 3: ")) # 7
        if nota3 >= 0 and nota3 <= 10:
            menor = nota1 

            if nota2 < menor:
                menor = nota2 # menor -> 3

            if nota3 < menor:
                menor = nota3

            media = (nota1 + nota2 + nota3 - menor) / 2

            print(f"A média das notas {nota1:.2f}, {nota2:.2f} e {nota3:.2f} é {media:.2f}")
        else:
            print(f"A Nota {nota3} é invalida!")
    
    else:
        print(f"A Nota {nota2} é invalida!")

else:
    print(f"A Nota {nota1} é invalida!")









 
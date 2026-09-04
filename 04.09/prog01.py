import os 
os.system("cls")


try:
    valor1 = int(input("Valor 1: "))
    valor2 = int(input("Valor 2: "))
    resp = valor1 / valor2
    print("Divisao: ", resp)

except ValueError as erro:
    print(erro)

except ZeroDivisionError:
    print("Nao ha divisao por 0 ")

except:
    print("falha, avise o programador ou chame a NASA para resolver")

else:
    print("Divisao: " , resp)

finally: 
    print("Obrigado por usar o nosso sistema")
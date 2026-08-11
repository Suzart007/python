# Parametros *args - Torna os argumentos voláteis

#          args = [34, 56, 34]    | num
def somar_numeros(*args) -> float: # args é uma lista
    soma = 0
    for num in args: # num = 34
        soma = soma + num # soma = 100

    return soma    



 
import os
os.system("clear")
soma = somar_numeros(34, 56, 34)
print("Soma:", soma)
soma = somar_numeros(34, 56, 34, 55, 77)
print("Soma:", soma)
soma = somar_numeros(34, 56)
print("Soma:", soma)
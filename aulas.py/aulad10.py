import os

# Casting – Mudança de tipo de variável
os.system("cls")  # windows 'cls'

valor = 23
resp = valor + valor
print(resp, type(valor))  # int

valor = str(valor)
resp = valor + valor
print(valor, type(valor))  # str

valor = float(valor)
resp = valor + valor
print(valor, type(valor))  # float

print(valor, type(valor))  # bool
valor = bool(valor) #true
print(valor)
resp = valor + valor # 
print(resp)
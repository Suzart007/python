import os
os.system("cls")


preco = float(input("digite o valor do maço: "))
q_m_d = float(input("diite a quantidade de maço de cigagos fumados por dia: "))
anos = float(input("digite por quantos anos: "))

dias = anos * 365

weed = ( dias * q_m_d * preco)

print(f"você gastou R$ {weed: .2f} com cigarros")
 
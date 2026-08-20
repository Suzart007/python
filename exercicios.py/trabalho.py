valor= input("Digite o valor: R$")
valor= float(valor)
porc= input("Digite o porcentagem: ")
porc= float(porc)
perc= valor * porc / 100
acresc= valor + perc
desc= valor - perc
print("percentual:", perc)
print("acrescimo:", acresc)
print("desconto:", desc)
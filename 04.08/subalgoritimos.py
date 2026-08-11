# PARÂMETROS (n1 e n2) - Informações recebidas do programa principal (fica no cabeçalho da construção do subalgoritmo)
def somar_numero(n1: float, n2: float) -> float:
    return n1 + n2

def p_somar_numero(n1: float, n2: float) -> None:
    print("Soma: ", n1 + n2)

# Uso no Principal
import os
os.system("clear")
# ARGUMENTOS (5 E 7) - Informações passadas ao subalgoritmo
# Chamando a função
soma = somar_numero(5, 7) # funcao: sempre escreva acompanhado de algo
print("Soma: ",soma)
# Chamando o procedimento
p_somar_numero(33, 55) # procedimento: sempre escreva isolado em uma linha
print(soma)

 
"""EXERCÍCIOS:
1. Escreva uma função que receba uma lista com elementos e retorne a quantidade de elementos
únicos (distintos) na lista.
 
2. Escreva uma função que receba uma lista por parâmetro e retorne a quantidade de elementos 
duplicados nesta lista
 
 
3. Escolha e apresente 5 frutas diferentes e coloque em um set.
Faça uma rotina que peça para o usuário adivinhar a fruta que foi sorteada.
Dê duas tentativas a ele. Caso ele acerte, exiba "Acertou na X tentativa a fruta sorteada".
Caso ele não acerte, informe: "Você não acertou, a fruta sorteada foi XXXXXXXX"."""


import os
os.system("cls")

def contar_elementos_unicos(lista):
    elementos_unicos = set(lista)
    return len(elementos_unicos)

# Exemplo de uso:
numeros = [1, 2, 2, 3, 4, 1, 4, 5, 7]
print("Elementos únicos:", contar_elementos_unicos(numeros))  



import os
os.system("cls")


def contar_elementos_duplicados(lista):
    return len(lista) - len(set(lista))

# Exemplo de uso:
frutas = ["maçã", "banana", "maçã", "laranja", "banana", "banana"]
print("Quantidade de duplicados:", contar_elementos_duplicados(frutas))  


import os
os.system("cls")


# 1. Definir o conjunto com 5 frutas
frutas = {"maçã", "banana", "laranja", "uva", "manga"}
print(f"Frutas disponíveis: {frutas}")

# 2. "Sortear" a fruta usando .pop() (retira um elemento aleatório do set)
fruta_sorteada = frutas.pop()

# 3. Estrutura de 2 tentativas
acertou = False
for tentativa in range(1, 3):
    palpite = input(f"\nTentativa {tentativa}: Qual fruta foi sorteada? ").strip().lower()
    
    if palpite == fruta_sorteada:
        print(f"Acertou na {tentativa}ª tentativa a fruta sorteada")
        acertou = True
        break

# 4. Exibir resultado se não acertou
if not acertou:
    print(f"Você não acertou, a fruta sorteada foi {fruta_sorteada}")



#jeito q o professor fez    

import os
os.system("cls")



def verificar_resposta(s: str, c:str)-> bool:
    return s == c

def exibir_frutas(f: set) -> None:
    lista_frutas = list(f)
    lista_frutas.sort()
    print("\nLista de frutas:")
    for fruta in lista_frutas:
        print("-", fruta)

def sorteia_fruta(f: set) -> str:
    copia_frutas = f.copy()
    return  copia_frutas.pop()

# Programa principal

frutas = {"banana", "goiaba", "uva", "melancia", "abacate"}

sorteada = sorteia_fruta(frutas)

tentativa = 1
import os
while tentativa <= 2:
  
    exibir_frutas(frutas) # exibe as frutas
    chute = input("Fruta: ")
    if verificar_resposta(sorteada, chute): # Se acertou
        print(f"\nAcertou na {tentativa}.a tentativa a fruta sorteada")
        break
    elif tentativa < 2: # caso ainda tenha tentativa
        print(f"\nErrou, tente novamente!")

    tentativa += 1

else:
    # Caso as alternativas se esgotem
    print(f"\nVocê não acertou, a fruta sorteada foi {sorteada}")



 
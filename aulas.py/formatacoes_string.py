#Concatenação
nome = "guilheme"
idade = 18
altura = 1.80

print("\nNome: " + nome + "\nIdade: " + str(idade) + "\nAltura: " + str(altura))




#forma 3:usando format()

print("\nNome: {0} \nIdade: {1} |nAltura: {2}" .format(nome, idade, altura))
      
    

    # formato 4: Usando  f print



os.system("clear")  # windows 'cls'

print(f"\nNome: {nome} \nIdade: {idade} \nAltura: {altura}")

print(f"Nome: {nome}", end = ",") # print exibe e pula de linha
print("Idade: {idade}", end = ",")
print("Altura: {altura}", end = ".")


#professor e oq eu nao consegui copiar

import os
os.system("clear") # windows 'cls'

nome = "Edson de Oliveira"
idade = 51
altura = 1.71
# FORMATAÇÃO DE STRINGS
# --- Forma 1: convencional (com vírgula) | separam todos tipos de dados
print(nome, idade, altura)
print("Nome:", nome, "Idade:", idade, "Altura:", altura)
print("\nNome:", nome, "\nIdade:", idade, "\nAltura:", altura) # \n - pula linha

# --- Forma 2: Concatenação: +
print(nome + str(idade) + str(altura))
print("\nNome:" + nome + "\nIdade:" + str(idade) + "\nAltura:" + str(altura))

# -- Forma 3: Usando format()
os.system("clear") # windows 'cls'
#                           0     1     2
print("\nNome: {0} \nIdade: {1} \nAltura: {2}".format(nome, idade, altura))
print("\nNome: {n} \nIdade: {i} \nAltura: {a}".format(n=nome, i=idade, a=altura)) #alias

# -- Forma 4: Usando f print
os.system("clear") # windows 'cls'
#                           0     1     2
print(f"\nNome: {nome} \nIdade: {idade} \nAltura: {altura}")

os.system("clear") # windows 'cls'
print(f"Nome: {nome}", end = ".") # print exibe e pula de linha
print(f"Idade: {idade}", end = ".")
print(f"Altura: {altura}", end = ".")

# Triple quotes: ''' texto ''' ou """ texto """
print("""
Professor, estou 
cansado de colocar
um monte de print
""")
os.system("clear") # windows 'cls'
print(f"""
    Nome.....: {nome}
    Idade....: {idade}
    Altura...: {altura}
""")
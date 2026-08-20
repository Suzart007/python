import os
os.system("cls")
# ------ DEFINIÇÃO DOS SUBALGORITMOS






# ------ PROGRAMA PRINCIPAL
# Estrutura do dicionario
aluno = {
    # 'key' : Value,
    'nome': 'Edson',
    'idade': 52,
    'curso': 'TDS',
}

# keys() -> cria uma lista com as keys do dicionario
print(aluno)
print(aluno.keys()) 

for k in aluno.keys():
    print(k)

for n, k in enumerate(aluno.keys(), 1):
    print(f"Campo {n} = {k}")

# values() -> cria uma lista com os values do dicionario
os.system("cls")
print(aluno)
print(aluno.values()) 

for v in aluno.values():
    print(v)

# items() -> cria uma lista de tupla com os dados
os.system("cls")
print(aluno)
print(aluno.items()) 

for k, v in aluno.items():
    print(f"{k.title():8}: {v}")

# clear() -> Apaga todos os items
aluno.clear()
print(aluno)





import os
os.system("cls") 

# ------ DEFINIÇÃO DOS SUBALGORITMOS
def exibir_aluno(a: dict) -> None:
    for k, v in a.items():
        print(f"{k.title():8}: {v}")

# Resolução do Exercício: Procedimento para preencher o dicionário
def preencher_aluno(a: dict) -> None:
    print("--- Preenchimento de Dados ---")
    a['nome'] = input("Digite o nome do aluno: ")
    a['idade'] = int(input("Digite a idade do aluno: "))
    a['curso'] = input("Digite o curso do aluno: ")

# ------ PROGRAMA PRINCIPAL
# Inicializando o dicionário vazio
aluno = {}

# Chamando o procedimento para o usuário preencher os dados
preencher_aluno(aluno)

print("\n--- Dados Registrados ---")
# Exibindo os dados preenchidos
exibir_aluno(aluno)
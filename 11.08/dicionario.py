import os
os.system("cls")

# Criando um dicionario vazio
dicionario = {} # ou dicionario = dict() -> cria um dicionario vazio


# Inserindo conteudos iniciais em um dicionario
aluno = {
    # 'key' : Value,
    'nome': 'Edson',
    'idade': 52,
    'curso': 'TDS',
}

print(aluno) # Acessar um dicionario na totalidade
print(aluno['nome']) # acessar um elemento do dicionario

# Métodos de manuseio de dicionarios
print(aluno['nome']) # acessar um elemento do dicionario
print(aluno.get('nome')) # Get retorna None se não existir a key, ou o value se a key existir
print(aluno.get('nota'))

if aluno.get('idade') == None:
    print("Key inexistente")
else:
    print("Key existente")
print(aluno)

# Editando o value
# aluno['idade'] = int(input("Idade: "))
print(aluno)

aluno = {
    # 'key' : Value,
    'nome': 'Edson',
    'idade': 52,
    'curso': 'TDS',
}

# Manipulando as keys
# Adicionando keys
os.system("cls")
print(aluno)
aluno['nota'] = 10.0
print(aluno)


# Removendo uma key
os.system("cls")
print(aluno)
aluno.pop('curso')
print(aluno)
#del aluno['idade']
#print(aluno)

if aluno.get("endereco") != None: # Se existir a key nome
    aluno.pop('endereco') # Existe, entao removo
else: # não existe nome
    print("endereco nao existe")

print(aluno)

 
import os 
os.system("cls")

# ======== MANIPULACAO DE ARQUIVO TXT
'''
modeos de abertura 
'w' | write = gravar em um arquivo (se existe o arq, ele sobregrava) 
'r' | read - le um arquivo
'a' | append - edita um arquivo
''  |


funcao open() abre um arquivo
sintaxe:
    <objetivo> = open ("nome_arquivo", "modo_abertura", ...)
'''

arquivo = open("arq01.txt", "w")
arquivo.write("gravei uma linha")
arquivo.close()
print("Arquivo gravado!")

#LEITURA DE ARQUIVOS 

print("------ Conteudo do arquivo")
arquivo = open("arq01.txt", "r", encoding="uft-8") 
print(arquivo.read().strip())
arquivo.close()
print("----------------------------------------")

#EDICAO DE ARQUIVO

arquivo = open("arq01.txt", "a" , encoding="utf-8")
arquivo.white ("Usando a edicao\n")
arquivo.close()



#ULTILIZANDO O MODO 

arquivo = open ("arq01.txt", "a+" encoding="utf-8")
arquivo = 


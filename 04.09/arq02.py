def cria_arquivo_exclusivo(na: str, msg: str) -> bool:
 
    try:    
        arquivo = open (nome_arquivo, "x", encoding="utf-8")
        arquivo.write("Grave uma linha, que emoção")
        arquivo.close()
    except FileExistsError:
        return False
    else:    
        return True

 #Principal

nome_arquivo = "arq07.txt"
mensagem = "Gravou"

if cria_arquivo_exclusivo(nome_arquivo, mensagem)
    print("Arquivo gerado com sucesso!")
else:
    print("Arquivo ja eiste, ")    
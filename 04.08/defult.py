def saudacao(nome: str = "Usuário", hora:int = 8) -> str:
    if hora < 12:
        msg = "Bom dia"
    elif hora < 18:
        msg = "Boa tarde"
    else:
        msg = "Boa noite"

    return f"{msg} {nome}, seja bem-vindo!"



# Principal
import os
os.system("clear")
print(saudacao("Maria",23))
print(saudacao("Julia"))
print(saudacao())
print(saudacao(hora = 14))
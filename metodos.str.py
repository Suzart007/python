import os
os.system("cls")

#Metodo de manipulacao de stringrs
nome = "guilherme suzart"

print(nome.upper()) # tudo em minusculo
print(nome.lower()) # tudo em maiusculo
print(nome.title()) # primeiras letras em maiuculo
print(nome.capitalize()) #primeira letra em maiusculo

nome = "     guilherme suzart     "
print("|" + nome + "|", len(nome), "caracteres")


novo = nome.strip()
print("|" + nome + "|", len(novo), "caracteres")

novo = nome.lstrip()
print("|" + nome + "|", len(novo), "caracteres")

novo = nome.rstrip()
print('|' + nome + '|', len(novo), "caracteres")


os.system("cls")
frase = "Aprendendo a manipular string"
print(frase)
new1 = frase.replace("e", "E")
print(new1)

new2 = frase.replace('manipular', "*******")
print(new2)

new3 = frase.replace('n', 'N', 2)
print(new3)

os.system("cls")
texto = "O split divide a string pelo argumento passado por parametro"
print(texto)
print(texto.split(), len(texto.split()), "partes")
print(texto.split('p'), len(texto.split('p')), "partes")

os.system("cls")
linguagens = ["Python", "Java", "C", "Javascript"]
print(linguagens)
print(" - ".join(linguagens))
print("".join(linguagens))
print(" ".join(linguagens))
print("|".join(linguagens))
print("banana".join(linguagens))


os.system("cls")


texto = "programacao em python em faculdade"
print(texto.find("em"))
print(texto.find("gra"))
print(texto.find("Edson"))

os.system("cls")

texto = "treinando o funcionamento do count()"
print(texto.count('o'))
print(texto.count(' do '))
print(texto.count('!'))
print("edson de oliveira".count('de'))


os.system("cls")

texto = "relatorio.pdf"
print(texto.endswith(".pdf"))
print(texto.endswith(".docx"))

os.system("cls")

texto = "1233"
print(texto.isdigit())
texto = "12a33"
print(texto.isdigit())
texto = "-1233"
print(texto.isdigit())
texto = "vi"
print(texto.isdigit())
texto = "VI"
print(texto.isdigit())

os.system("cls")


texto = "Python"
print(texto.isalpha())
texto = "Pyt3hon"
print(texto.isalnum())
texto = "Python!"
print(texto.isalnum())


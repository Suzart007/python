def contar_palavras(texto: str) -> dict:
    if not texto.strip():
        return {}

    palavras = texto.lower().split()
    contagem = {}

    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1

    return contagem


def substituir_multiplas(texto: str, subs: dict) -> str:
    for antiga, nova in subs.items():
        texto = texto.replace(antiga, nova)

    return texto


def remover_duplicadas(texto: str) -> str:
    palavras = texto.split()

    if not palavras:
        return ""

    resultado = [palavras[0]]

    for i in range(1, len(palavras)):
        if palavras[i] != palavras[i - 1]:
            resultado.append(palavras[i])

    return " ".join(resultado)
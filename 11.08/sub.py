def obter_extremos(lista: list) -> list:
    primeiro = lista[:1]
    ultimo = lista[-1:]

    return [primeiro[0], ultimo[0]]


def inverter_texto(texto: str) -> str:
    return texto[::-1]


def analisar_frase(frase: str) -> tuple[str, int, int]:
    frase = frase.strip()
    palavras = frase.split()

    quantidade_caracteres = len(frase)
    quantidade_palavras = len(palavras)

    return frase, quantidade_caracteres, quantidade_palavras


def substituir_palavra(frase: str, antiga: str, nova: str) -> str:
    resultado = frase.replace(antiga, nova)

    return resultado


def filtrar_intervalo(lista: list, inicio: int, fim: int) -> list:
    return lista[inicio:fim]
def adicionar_produto(produtos: dict) -> None:
    codigo = input("Código: ").strip()

    if codigo in produtos:
        print("Existe")
        return

    nome = input("Nome: ").strip()

    try:
        qtd = int(input("Qtd: "))
        preco = float(input("Preço: "))

        if qtd >= 0 and preco >= 0:
            produtos[codigo] = {
                'nome': nome,
                'qtd': qtd,
                'preco': preco
            }

            print("Adicionado")

    except:
        print("Números inválidos")


def registrar_entrada(produtos: dict) -> None:
    codigo = input("Código: ").strip()

    if codigo in produtos:
        try:
            qtd = int(input("Qtd: "))

            produtos[codigo]['qtd'] += qtd

            print("Entrada registrada")

        except:
            print("Inválido")


def registrar_saida(produtos: dict) -> None:
    codigo = input("Código: ").strip()

    if codigo in produtos:
        try:
            qtd = int(input("Qtd: "))

            if produtos[codigo]['qtd'] >= qtd:
                produtos[codigo]['qtd'] -= qtd
                print("Saída registrada")
            else:
                print(f"Insuficiente! Tem: {produtos[codigo]['qtd']}")

        except:
            print("Inválido")


def estoque_baixo(produtos: dict) -> None:
    for codigo, dados in produtos.items():
        if dados['qtd'] < 5:
            print(f"{dados['nome']}: {dados['qtd']} un")


def valor_total(produtos: dict) -> None:
    total = sum(d['qtd'] * d['preco'] for d in produtos.values())

    print(f"Total: R$ {total:.2f}")
def adicionar_contato(contatos: dict) -> None:
    nome = input("Nome: ").strip()

    if nome in contatos:
        print("Já existe!")
        return

    telefone = input("Telefone: ").strip()
    email = input("Email: ").strip()

    contatos[nome] = {
        'telefone': telefone,
        'email': email
    }

    print("Adicionado!")


def listar_contatos(contatos: dict) -> None:
    if not contatos:
        print("Vazio")
        return

    for i, (nome, dados) in enumerate(contatos.items(), 1):
        print(f"{i}. {nome}: {dados['telefone']}")


def buscar_contato(contatos: dict) -> None:
    nome = input("Nome: ").strip()

    if nome in contatos:
        print(contatos[nome])
    else:
        print("Não encontrado")


def editar_telefone(contatos: dict) -> None:
    nome = input("Nome: ").strip()

    if nome in contatos:
        contatos[nome]['telefone'] = input("Novo tel: ")
        print("Atualizado")


def remover_contato(contatos: dict) -> None:
    nome = input("Nome: ").strip()

    if nome in contatos:
        contatos.pop(nome)
        print("Removido")
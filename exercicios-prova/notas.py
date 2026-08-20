def adicionar_aluno(turma: dict) -> None:
    nome = input("Nome: ").strip()

    if nome in turma:
        print("Existe")
        return

    turma[nome] = {}
    print("Adicionado")


def adicionar_nota(turma: dict) -> None:
    nome = input("Nome: ").strip()

    if nome not in turma:
        print("Não existe")
        return

    disciplina = input("Disciplina: ").strip()

    try:
        nota = float(input("Nota (0-10): "))

        if 0 <= nota <= 10:
            turma[nome][disciplina] = nota
            print("Adicionada")
        else:
            print("Inválida (0-10)")

    except:
        print("Digite número")


def calcular_media(notas: dict) -> float:
    if not notas:
        return 0.0

    return sum(notas.values()) / len(notas)


def listar_medias(turma: dict) -> None:
    for nome, notas in turma.items():
        if notas:
            media = calcular_media(notas)
            print(f"{nome}: {media:.2f}")


def alunos_reprovados(turma: dict) -> None:
    for nome, notas in turma.items():
        if notas and calcular_media(notas) < 6.0:
            print(f"{nome}: {calcular_media(notas):.2f}")


def remover_aluno(turma: dict) -> None:
    nome = input("Nome: ").strip()

    if nome in turma:
        turma.pop(nome)
        print("Removido")
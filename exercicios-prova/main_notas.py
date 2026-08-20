import os
os.system("cls")

from notas import *

turma = {}

while True:
    print("1. Aluno")
    print("2. Nota")
    print("3. Médias")
    print("4. Reprovados")
    print("5. Remover")
    print("0. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        adicionar_aluno(turma)

    elif opcao == "2":
        adicionar_nota(turma)

    elif opcao == "3":
        listar_medias(turma)

    elif opcao == "4":
        alunos_reprovados(turma)

    elif opcao == "5":
        remover_aluno(turma)

    elif opcao == "0":
        break
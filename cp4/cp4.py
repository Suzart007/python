funcionarios = {}

while True:
    print("=" * 30)
    print("M E N U")
    print("=" * 30)
    print("0 - SAIR")
    print("1 - Cadastrar Funcionários")
    print("2 - Consultar Funcionários")
    print("3 - Editar Funcionários")
    print("4 - Excluir Funcionários")
    print("5 - Listar Funcionários")
    print("=" * 30)

    opcao = input("Escolha: ")

    if opcao == "0":
        print("Saindo do programa...")
        break

    # Cadastro
    elif opcao == "1":
        print("CADASTRANDO FUNCIONARIO")
        print("=" * 30)
        cpf = input("CPF .....: ")

        if cpf in funcionarios:
            print("Funcionário já existe!")
        else:
            nome = input("Nome ....: ")
            salario = float(input("Salário .: "))
            funcionarios[cpf] = {"nome": nome, "salario": salario}
            print("Cadastrado com sucesso!")

    # Consulta
    elif opcao == "2":
        print("CONSULTANDO FUNCIONARIO")
        print("=" * 30)
        cpf = input("CPF .....: ")

        if cpf in funcionarios:
            dados = funcionarios[cpf]
            print("CPF.....: ", cpf)
            print("Nome....: ", dados["nome"])
            print("Salário.: ", dados["salario"])
        else:
            print("Funcionário inexistente!")

    # Alteração
    elif opcao == "3":
        print("EDITANDO FUNCIONARIO")
        print("=" * 30)
        cpf = input("CPF .....: ")

        if cpf in funcionarios:
            funcionario = funcionarios[cpf]
            print("CPF.....: ", cpf)
            print("Nome....: ", funcionario["nome"])
            print("Salário.: ", funcionario["salario"])
            print()
            print("Edite os campos:")

            nome_novo = input("Nome....: ")
            salario_novo = float(input("Salário.: "))

            funcionarios[cpf] = {"nome": nome_novo, "salario": salario_novo}
            print("Editado com sucesso!")
        else:
            print("Funcionário inexistente!")

    # Exclusão
    elif opcao == "4":
        print("EXCLUINDO FUNCIONARIO")
        print("=" * 30)
        cpf = input("CPF .....: ")

        if cpf in funcionarios:
            funcionario = funcionarios[cpf]
            print("CPF.....: ", cpf)
            print("Nome....: ", funcionario["nome"])
            print("Salário.: ", funcionario["salario"])
            print()

            confirmacao = input("Confirma a exclusão do funcionário [S/N] ")

            if confirmacao.upper() == "S":
                del funcionarios[cpf]
                print("Funcionário excluído com sucesso!")
            else:
                print("Exclusão cancelada.")
        else:
            print("Funcionário inexistente!")

    # Lista
    elif opcao == "5":
        print("LISTANDO FUNCIONÁRIOS")
        print("CPF          NOME                 SALARIO")
        print("=" * 40)

        if funcionarios:
            for cpf, funcionario in funcionarios.items():
                print(f"{cpf:<12} | {funcionario['nome']:<20} | R$ {funcionario['salario']:>10.2f}")
            print("=" * 40)
        else:
            print("Nenhum funcionário cadastrado.")

    else:
        print("Opção inválida.")

    input("Pressione alguma tecla para continuar...")
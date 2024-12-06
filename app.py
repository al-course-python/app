import os


# Init
def exibir_nome_programa():
    print(
        """  
┏━━━┓╋╋┏┓╋╋╋╋╋╋╋┏━━━┓
┃┏━┓┃╋╋┃┃╋╋╋╋╋╋╋┃┏━━┛
┃┗━━┳━━┫┗━┳━━┳━┓┃┗━━┳┓┏┳━━┳━┳━━┳━━┳━━┓
┗━━┓┃┏┓┃┏┓┃┏┓┃┏┛┃┏━━┻╋╋┫┏┓┃┏┫┃━┫━━┫━━┫
┃┗━┛┃┏┓┃┗┛┃┗┛┃┃╋┃┗━━┳╋╋┫┗┛┃┃┃┃━╋━━┣━━┃
┗━━━┻┛┗┻━━┻━━┻┛╋┗━━━┻┛┗┫┏━┻┛┗━━┻━━┻━━┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗┛
      """
    )


# Limpar terminal
def clear():
    os.system("cls")


# Finalizar app
def encerrar_app():
    clear()
    print("Encerrando aplicativo..")


# Voltar ao menu
def voltar_menu():
    input("\nDigite uma tecla para voltar ao menu principal")
    main()


# Print opções
def escolher_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alterar situação")
    print("4. Sair\n")


# Opção inválida
def mensagem_opcao_invalida():
    print("Opção inválida!\n")
    voltar_menu()


# Restaurantes
restaurantes: list[dict[str, str | bool]] = []


# New restaurantes
def cadastrar_novo_restaurante():
    clear()
    print("Cadastro de novos restaurantes\n")
    nome = input("Digite o nome do restaurante a ser cadastrado: ")
    categoria = input("Digite o tipo de comida nesse restaurante: ")

    novo_restaurante: dict[str, str | bool] = {
        "nome": nome,
        "categoria": categoria,
        "ativo": True,
    }

    restaurantes.append(novo_restaurante)

    print(f"\nO restaurante {nome} foi cadastrado com sucesso!")
    voltar_menu()


# Print restaurantes
def listar_restaurantes():
    clear()
    print("Listando restaurantes\n")

    for restaurante in restaurantes:
        print(f"Nome: {restaurante["nome"]}")
        print(f"Categoria: {restaurante["categoria"]}")
        if restaurante["ativo"]:
            print("Situação: Ativo")
        else:
            print("Situação: Inativo")
    voltar_menu()


# Ativar resturantes
def alterar_situacao():
    clear()
    print("Alterar situação do restaturante restaurantes\n")

    print("Restaurantes:")
    for restaurante in restaurantes:
        print(f"\nNome: {restaurante["nome"]}")

    nome_restaurante = input("\nDigite o nome do restaurante que deseja alterar: ")

    for restaurante in restaurantes:
        if (
            isinstance(restaurante["nome"], str)
            and nome_restaurante.lower() == restaurante["nome"].lower()
        ):
            restaurante["ativo"] = not restaurante["ativo"]

            estado = "ativo" if restaurante["ativo"] else "inativo"
            print(f"\nO restaurante '{nome_restaurante}' foi alterado para {estado}.")

            return True

    print("\nRestaurante não encontrado")
    return False


# Exibir opções
def exibir_opcoes():
    try:
        input_opcao = int(input("Escolha uma opção: "))

        if input_opcao == 1:
            cadastrar_novo_restaurante()
        elif input_opcao == 2:
            if restaurantes == []:
                print("\nNão existem restaurantes cadastrados\n")
            else:
                listar_restaurantes()
        elif input_opcao == 3:
            if restaurantes == []:
                print("\nNão existem restaurantes cadastrados\n")
            else:
                alterar_situacao()
        elif input_opcao == 4:
            encerrar_app()
        else:
            mensagem_opcao_invalida()
    except:
        mensagem_opcao_invalida()


# Main()
def main():
    exibir_nome_programa()
    escolher_opcoes()
    exibir_opcoes()


# Val
if __name__ == "__main__":
    main()

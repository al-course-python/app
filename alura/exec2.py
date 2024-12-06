import os

os.system("cls")

# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.


def par_ou_impar():
    num = int(input("Insira um número: "))

    if num % 2 == 0:
        print(f"{num} é um número par.\n")
    else:
        print(f"{num} é um número impar.\n")


# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.


def faixa_etaria():
    idade = int(input("Insira sua idade: "))

    if idade >= 0 and idade <= 12:
        print("Você é Criança\n")
    elif idade >= 13 and idade < 18:
        print("Você é Adolescente\n")
    else:
        print("Você é Adulto\n")


# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.


def validar_user():
    user_db = "root"
    senha_db = "password"

    user = input("Escreva seu nome de usuário: ")
    senha = input("Escreva sua senha: ")

    if user != user_db:
        print("\nUsuário inválido!")
    elif senha != senha_db:
        print("\nSenha inválida!")
    else:
        print("\nLogin realizado com sucesso..")


# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.


def plano_cartesiano():
    x = int(input("Insira as coordernadas de X: "))
    y = int(input("Insira as coordernadas de Y: "))

    if x > 0 and y > 0:
        print("Primeiro Quadrante")
    elif x < 0 and y > 0:
        print("Segundo Quadrante")
    elif x < 0 and y < 0:
        print("Terceiro Quadrante")
    elif x > 0 and y < 0:
        print("Quarto Quadrante")
    else:
        print("O ponto está localizado no eixo ou origem.")

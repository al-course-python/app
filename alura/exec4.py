# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

pessoas: list[dict[str, str | int]] = [
    {"nome": "João", "idade": 19, "cidade": "São Paulo"},
    {"nome": "Erik", "idade": 22, "cidade": "São Paulo"},
    {"nome": "Fabrício", "idade": 35, "cidade": "São Paulo"},
]


def mensagem(texto: str):
    print(f"\n{'*' * len(texto)}")
    print(texto)
    print(f"{'*' * len(texto)}\n")


def print_pessoas():
    print("\nPessoas:")
    for pessoa in pessoas:
        print(f"Nome: {pessoa["nome"]}")
        print(f"Idade: {pessoa["idade"]}")
        print(f"Cidade: {pessoa["cidade"]}\n")


print_pessoas()


# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);

mensagem("Alterando campo idade")
pessoas[2].update({"idade": 23})
print(f"\nNome: {pessoas[2]["nome"]}")
print(f"Idade: {pessoas[2]["idade"]}")
print(f"Cidade: {pessoas[2]["cidade"]}")


# Adicione um campo de profissão para essa pessoa;

mensagem("Adicionando campo Profissão")
pessoas[2].update({"profissao": "Product Owner"})
print(f"\nNome: {pessoas[2]["nome"]}")
print(f"Idade: {pessoas[2]["idade"]}")
print(f"Cidade: {pessoas[2]["cidade"]}")
print(f"Profissão: {pessoas[2]["profissao"]}")

# Remova um item do dicionário.

mensagem("Depois de remover uma pessoa")
pessoas.remove(pessoas[2])
print_pessoas()


# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
mensagem("Números ao quadrado")
numeros_quadrados = {x: x**2 for x in range(1, 6)}

for numero, quadrado in numeros_quadrados.items():
    print(f"Número {numero} ao quadrado é igual à: {quadrado}")

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.


def buscar_idade():
    idade = int(input("\nDigite a idade que deseja buscar: "))
    for pessoa in pessoas:
        if pessoa["idade"] == idade:
            print(f"\n{pessoa["nome"]} tem a idade buscada")
            return True
    print("\nNinguém possuí essa idade")
    return False


buscar_idade()


# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

mensagem("Frequência de palavras")
frase = input("Digite uma frase: \n")
contagem_palavras: dict[str, int] = {}
palavras = frase.split()

print("\nA frequência com que cada palavra aparece:\n")
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

for palavra, frequencia in contagem_palavras.items():
    print(f"A palavra '{palavra}' aparece: {frequencia} vez(es)")

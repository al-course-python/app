# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ["João", "Erik", "Pedro", "Fabrício"]
anos = ["2005", "2024"]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

herois = ["Homem de ferro", "Capitão América", "Hulk", "Thor"]

print("\nIterando lista de Heróis:")
for heroi in herois:
    print(f"{heroi}")

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

print("\nSomando números impáres")
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
    print(f"{soma_impares}")

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

ordem_decrescente = ", ".join(str(i) for i in range(10, 0, -1)) + "."
print("\nIterando em ordem decrescente:")
print(ordem_decrescente)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

n = int(input("\n\nInsira um número: "))
for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

print("\nSoma de uma lista de números:")
soma = 0
try:
    for numero in numeros:
        soma += numero
    print(f"A soma dos números é igual à: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

print("\nMédia de valores em lista")
soma_media = 0

try:
    for numero in numeros:
        soma_media += numero
    print(f"A média dos valores é: {soma_media / len(numeros)}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

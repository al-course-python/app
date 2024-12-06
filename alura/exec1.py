# 1 - Imprima a frase: Python na Escola de Programação da Alura.

print("Python na Escola de Programação da Alura.\n")

# 2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.

nome = "João"
idade = 19
print(f"Meu nome é {nome} e tenho {idade}\n")

# 3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:

print(
    """
      A
      L
      U
      R
      A
      """
)

# 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:

pi = 3.14159
# print(f"O valor arredondado de pi é: {pi:.2f}")
print(f"O valor arredondado de pi é: {round(pi, 2)}")

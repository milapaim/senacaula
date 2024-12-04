# Função para verificar se um caractere é consoante
def is_consonant(char):
    vowels = 'aeiouAEIOU'
    return char.isalpha() and char not in vowels

# Inicialização do vetor e contagem de consoantes
characters = []
consonants = []

# Lendo 10 caracteres
print("Digite 10 caracteres:")
for i in range(10):
    while True:
        char = input(f"Caractere {i + 1}: ").strip()
        if len(char) == 1 and char.isalpha():  # Verifica se é um único caractere alfabético
            characters.append(char)
            if is_consonant(char):
                consonants.append(char)
            break
        else:
            print("Entrada inválida. Por favor, insira apenas um caractere alfabético.")

# Exibindo resultados
print("Consoantes lidas:", consonants)
print("Quantidade de consoantes:", len(consonants))

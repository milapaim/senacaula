# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra: ")

# Inicializa o contador de vogais
contador = 0

# Itera sobre cada letra da palavra
for letra in palavra:
    # Verifica se a letra é uma vogal
    if letra.lower() in "aeiou":
        contador += 1

# Exibe o resultado
print("A palavra '{}' tem {} vogais.".format(palavra, contador))

# Verifica se há ou não vogais na palavra
if contador > 0:
    print("True")  # Há vogais
else:
    print("False")  # Não há vogais

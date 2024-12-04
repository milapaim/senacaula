def eh_palindromo(texto):
    # Remove espaços e converte para minúsculas
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    # Verifica se o texto é igual ao seu reverso
    return texto_limpo == texto_limpo[::-1]

# Teste
entrada = input("Digite uma palavra ou frase: ")
if eh_palindromo(entrada):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")

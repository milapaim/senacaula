# Inicializa uma lista vazia
numeros = []

print("Digite 10 números inteiros:")
for i in range(10):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

print("\nOs números digitados foram:")
for numero in numeros:
    print(numero)

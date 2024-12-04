# Inicializando os vetores
numeros = []
pares = []
impares = []

# Lendo 20 números inteiros
for i in range(20):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
    
    # Verificando se o número é par ou ímpar e armazenando nos vetores correspondentes
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Imprimindo os três vetores
print("\nVetor de números:", numeros)
print("Vetor de números pares:", pares)
print("Vetor de números ímpares:", impares)

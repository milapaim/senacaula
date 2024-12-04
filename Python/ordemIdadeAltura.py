# Listas para armazenar idades e alturas
idades = []
alturas = []

for i in range(5):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    altura = float(input(f"Digite a altura da pessoa {i + 1} (em metros): "))
    idades.append(idade)
    alturas.append(altura)

for i in range(4, -1, -1):  # Itera de 4 a 0
    print(f"Pessoa {i + 1}: Idade = {idades[i]}, Altura = {alturas[i]} m")


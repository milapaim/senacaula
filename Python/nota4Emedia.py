# Inicializa uma lista para armazenar as notas
notas = []

# Lê as 4 notas do usuário
for i in range(4):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("\nNotas:")
for i, nota in enumerate(notas, start=1):
    print(f"Nota {i}: {nota:.2f}")

print(f"\nMédia: {media:.2f}")

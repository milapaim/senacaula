# Inicializando a lista para armazenar as médias dos alunos
medias = []

# Coletando as notas de cada aluno
for aluno in range(1, 11):  # 10 alunos
    notas = []  # Lista para armazenar as 4 notas do aluno
    print(f"\nAluno {aluno}:")
    
    # Lendo as 4 notas do aluno
    for i in range(1, 5):
        while True:
            try:
                nota = float(input(f"Digite a nota {i} do aluno {aluno}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    
    # Calculando a média das 4 notas
    media = sum(notas) / len(notas)
    medias.append((aluno, media))

# Imprimindo os alunos com média igual ou superior a 7,5
print("\nAlunos com média igual ou acima de 7,5:")
for aluno, media in medias:
    if media >= 7.5:
        print(f"Aluno {aluno} - Média: {media:.2f}")

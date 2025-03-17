# Solicita a quantidade de alunos
quantidade_alunos = int(input("Quantos alunos? "))

# Listas para armazenar nomes e notas
nomes = []
notas = []

# Cadastro de alunos e notas
for i in range(quantidade_alunos):
    nome = input(f"Nome do aluno {i+1}: ")
    nota = float(input(f"Nota do aluno {i+1}: "))
    nomes.append(nome)
    notas.append(nota)

# Calcula a média da turma
media_turma = sum(notas) / quantidade_alunos

# Identifica alunos acima da média
acima_da_media = [nomes[i] for i in range(quantidade_alunos) if notas[i] > media_turma]

# Ordena os alunos por nota (do maior para o menor)
alunos_ordenados = sorted(zip(notas, nomes), reverse=True)

# Exibe a média da turma
print(f"\nMédia da turma: {media_turma:.2f}")

# Exibe os alunos acima da média
print("\nAlunos acima da média:")
for aluno in acima_da_media:
    print(f"- {aluno}")

# Exibe a lista ordenada por nota
print("\nLista ordenada por nota:")
for i, (nota, nome) in enumerate(alunos_ordenados, start=1):
    print(f"{i}. {nome} - {nota:.2f}")

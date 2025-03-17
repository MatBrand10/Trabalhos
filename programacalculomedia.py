# Solicita as três notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Verifica se o aluno foi aprovado
if media >= 6:
    print(f"Média: {media:.2f} - Aprovado! 🎉")
else:
    print(f"Média: {media:.2f} - Reprovado. 😞")
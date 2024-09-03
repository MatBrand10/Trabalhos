def contar_letra_a(texto):
    # Conta o número de ocorrências da letra 'a' ou 'A' na string
    contagem = texto.lower().count('a')
    return contagem

# Solicita a entrada do usuário
entrada = input("Digite a string para verificar: ")

# Obtém a contagem da letra 'a'
quantidade_a = contar_letra_a(entrada)

# Exibe o resultado
print(f"A letra 'a' aparece {quantidade_a} vez(es) na string.")
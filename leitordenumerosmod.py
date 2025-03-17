# Cria uma lista vazia para armazenar os números
numeros = []

# Solicita 10 números inteiros ao usuário
for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

# Calcula a média dos números
media = sum(numeros) / len(numeros)

# Exibe os números na ordem inversa
print("\nNúmeros na ordem inversa:")
for num in reversed(numeros):
    print(num)

# Exibe a média dos números
print(f"\nMédia dos valores: {media:.2f}")

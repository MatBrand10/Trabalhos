# Cria uma lista vazia para armazenar os números
numeros = []

# Solicita 10 números inteiros ao usuário
for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

# Exibe os números na ordem inversa
print("\nNúmeros na ordem inversa:")
for num in reversed(numeros):
    print(num)

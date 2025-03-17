# Cria uma lista vazia para armazenar os números
numeros = []

# Solicita 5 números ao usuário
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Determina o maior e o menor número
maior = max(numeros)
menor = min(numeros)

# Exibe os resultados
print(f"\nNúmeros digitados: {numeros}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")

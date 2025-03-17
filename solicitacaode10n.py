# Lista para armazenar os números
numeros = []

# Contadores para pares e ímpares
pares = 0
impares = 0

# Solicita 10 números ao usuário
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

    # Verifica se é par ou ímpar
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

# Exibe os resultados
print(f"\nNúmeros digitados: {numeros}")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")

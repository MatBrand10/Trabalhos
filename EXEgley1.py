# 01 - Média de 5 números
numeros = []
for i in range(5):
    while True:
        try:
            numero = float(input(f"Digite o {i+1}º número: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

media = sum(numeros) / len(numeros)
print(f"A média é: {media:.2f}")
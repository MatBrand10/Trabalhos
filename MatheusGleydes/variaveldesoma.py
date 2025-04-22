soma = 0
while True:
    numero = int(input("Digite um numero inteiro (0 para sair):"))
    if numero == 0:
        break
    soma += numero
print(f" A soma dos numero é {soma}")
numero = int(input("Digite o numero inteiro positivo:"))

soma = 0

if numero <=0:
    print("Por favor, insira um numero inteiro positivo.")
else:
    i = 2
    while i <= numero:
        soma += i
        i += 2
    
    print(f"A soma dos numeros pares de 1 até {numero} é: {soma}")
def pertence_fibonacci(num):
    # Função para verificar se num pertence à sequência de Fibonacci
    if num < 0:
        return False
    
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

# Solicita ao usuário um número
try:
    numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
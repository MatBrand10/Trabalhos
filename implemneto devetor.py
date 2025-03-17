# Cria uma lista vazia para armazenar os números
numeros = []

# Solicita a quantidade de elementos no vetor
quantidade = int(input("Quantos números deseja inserir no vetor? "))

# Solicita os números ao usuário
for i in range(quantidade):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Solicita o número a ser contado
num_contar = int(input("\nDigite o número que deseja contar: "))

# Conta as ocorrências do número no vetor
quantidade_ocorrencias = numeros.count(num_contar)

# Exibe o resultado
print(f"\nO número {num_contar} aparece {quantidade_ocorrencias} vezes no vetor.")

# Solicita a temperatura em Celsius
celsius = float(input("Digite a temperatura em Celsius: "))

# Converte para Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Exibe o resultado
print(f"{celsius:.2f}°C equivale a {fahrenheit:.2f}°F")

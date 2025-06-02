produtos = {
    "Agasalho de Inverno": 58.50,
    "Cama Almofadada": 125.00,
    "Ração de 10kg": 525.00,
    "Petisco de Gato": 28.50,
    "Escova de Banho": 46.00,
}
print("Usando items():")
for chave, valor in produtos.items():
    print(f"Produto: {chave}, Valor: {valor}")
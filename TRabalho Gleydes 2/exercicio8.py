produtos = []
print("Insira produtos e preços. Digite 'fim' para encerrar.")
while True:
    prod = input("Produto: ")
    if prod.lower() == "fim":
        break
    preco = input("Preço: ")
    if preco.lower() == "fim":
        break
    produtos.append({"Produto": prod, "Preço": preco})
print("Lista de produtos inseridos:")
for p in produtos:
    print(p)

produtos_fornecedores = [
    {"Produto": "Ração Royal Canim – 10 kg", "Fornecedor": "Pet do Rei", "Valor": 495.00},
    {"Produto": "Ração Origens – 10 kg", "Fornecedor": "Walmak", "Valor": 183.00},
    {"Produto": "Ração Golden – 10 kg", "Fornecedor": "Mercadão das Rações", "Valor": 180.00},
    {"Produto": "Ração Gran Plus – 10 kg", "Fornecedor": "Pet do Animal", "Valor": 274.00},
    {"Produto": "Ração Whiskas – 10 kg", "Fornecedor": "Paraiso das Rações", "Valor": 165.00}
]
print("\nProduto\t\t\tFornecedor\t\t\tValor")
for item in produtos_fornecedores:
    print(f"{item['Produto']}\t{item['Fornecedor']}\t{item['Valor']}")
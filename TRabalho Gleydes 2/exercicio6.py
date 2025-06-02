produtos = {
    "Ração": {"quantidade": 2000, "valor": 495.00},
    "Escova": {"quantidade": 50, "valor": 32.00},
    "Touca": {"quantidade": 1500, "valor": 45.00},
    "Vasilha de Água": {"quantidade": 375, "valor": 27.50},
    "Coleira": {"quantidade": 400, "valor": 80.00}
}

print("Produto".ljust(18), "Quantidade".ljust(12), "Valor")
for nome, info in produtos.items():
    print(nome.ljust(18), str(info['quantidade']).ljust(12), info['valor'])
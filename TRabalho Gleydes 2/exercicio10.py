estoque = {
    "Banana": {"nome": "Açaí com Banana", "quantidade": 20, "valor": 15.00},
    "Morango": {"nome": "Açaí com Morango", "quantidade": 15, "valor": 25.00},
    "Granola": {"nome": "Açaí com Granola", "quantidade": 35, "valor": 17.00}
}

print("Controle de estoque de Açaí")
while True:
    print("\nProdutos disponíveis:")
    for chave, info in estoque.items():
        print(f"- {info['nome']} (digite: {chave}) - R$ {info['valor']} | Estoque: {info['quantidade']}")
    prod = input("Qual produto deseja comprar? (ou 'fim' para encerrar): ")
    if prod == "fim":
        break
    if prod in estoque:
        try:
            qtd = int(input("Quantidade desejada: "))
        except ValueError:
            print("Digite um número válido.")
            continue
        if qtd <= estoque[prod]["quantidade"]:
            total = qtd * estoque[prod]["valor"]
            estoque[prod]["quantidade"] -= qtd
            print(f"Compra realizada! Total a pagar: R$ {total:.2f}")
        else:
            print("Quantidade insuficiente em estoque.")
    else:
        print("Produto não encontrado.")

print("\nEstoque final:")
print("Produto".ljust(20), "Quantidade")
for info in estoque.values():
    print(info['nome'].ljust(20), info['quantidade'])
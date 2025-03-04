# 11 - Cálculo de desconto
preco = float(input("Digite o preço: "))
percentual = float(input("Digite o percentual de desconto: "))
desconto = preco * (percentual / 100)
preco_final = preco - desconto
print(f"Desconto: R$ {desconto:.2f}, Preço final: R$ {preco_final:.2f}")

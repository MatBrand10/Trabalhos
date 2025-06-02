produtos = {
    "Escova de Banho": 38.50,
    "serviço de Banho": 125.00,
    "Luva": 32.00,
    "Petisco de cao": 55.00,
    "Cobertor Microfibra": 59.90,
    
}
produtos_keys = list(produtos.keys())
if len(produtos_keys) >= 3:
    del produtos[produtos_keys[2]]
print("Produtos após remoção do 3º item:")
for k, v in produtos.items():
    print(f"{k}: {v}")
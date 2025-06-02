produtos = {
    "Ração": 513.00,
    "Coleira de Passeio": 60.00,
    "Shampoo": 25.00,
    "Toca de Plastico": 105.00,
    "Cobertor": 86.00,
    "Serviço de Banho": 120.00
}
while True:
    busca = input('Digite o produto para pesquisar (ou "fim" para encerrar): ')
    if busca.lower() == "fim":
        break
    if busca in produtos:
        print(f"{busca} está na lista com valor R$ {produtos[busca]}")
    else:
        print(f"{busca} não encontrado na lista.")
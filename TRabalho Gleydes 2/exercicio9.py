agenda = {}
while True:
    print("Menu: 1-Cadastrar | 2-Buscar | 3-Listar | 4-Sair")
    op = input("Escolha uma opção: ")
    if op == "1":
        nome = input("Nome: ")
        tel = input("Telefone: ")
        agenda[nome] = tel
        print("Contato cadastrado.")
    elif op == "2":
        nome = input("Nome a buscar: ")
        tel = agenda.get(nome)
        if tel:
            print(f"Telefone de {nome}: {tel}")
        else:
            print("Contato não encontrado.")
    elif op == "3":
        print("Lista de contatos:")
        for n, t in agenda.items():
            print(f"{n}: {t}")
    elif op == "4":
        print("Saindo da agenda.")
        break
    else:
        print("Opção inválida.")
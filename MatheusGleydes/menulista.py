menu = ["Padaria", "Açougue", " Rotisseria", "Bebidas"]

while True:
    escolhido = int(input("Digite um opção do Menu: (1 a 4 ou 0 para sairdo menu)" ))
    if escolhido == 0:
        break
    print(" Você escolheu o menu: %s" % (menu[escolhido-1]))
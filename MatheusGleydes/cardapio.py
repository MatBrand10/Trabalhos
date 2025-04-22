import random

cod = 0
qtde = 0
valor_cf = 0.0
valor_bq = 0.0
valor_kibe = 0.0
valor_ec = 0.0
valor_ln = 0.0
valor_br = 0.0
valor_rf = 0.0
total = 0.0
nome_cli = ""
pedido = 0
status_pedido = ""

print("--------------------------------------------------------")
print("                 CARDAPIO LANCHONETE"                    )
print("--------------------------------------------------------")
print("CODIGO           PRODUTO             PREÇO(UNIDADE)     ")
print("--------------------------------------------------------")
print("100          COXINHA DE FRANGO       R$0,85")
print("101          BOLINHA DE QUEIJO       R$0,85")
print("102          KIBE                    R$0,95")
print("103          ESFIRRA DE CARNE        R$0,95")
print("104          LANCHE NATURAL          R$8,00")
print("105          BEIRUTE                 R$8,00")
print("106          REFRIGERANTE            R$5,50")
print("--------------------------------------------------------")
print("")

nome_cli = input("INFORME O NOME DO CLIENTE")
pedido = random.randint(1, 50)
print(" NUMERO DO PEDIDO:", pedido)
print("")

status_pedido = input(f"REGISTRAR PEDIDO {pedido}? S/N")

total = 0.0

while status_pedido != "N":
    cod = int(input("SELECIONE SEU PRODUTO:"))
    
    if cod == 100:
        print(nome_cli, "ESCOLHEU COXINHA DE FRANGO :)")
        qtde = int(input("INFORME A QUANTIDADE: "))
        valor_cf = 0.85 * qtde
        print(f"O VALOR DE COXINHA DE FRANGO É R${valor_cf:.2f}")
    elif cod == 101:
        print(nome_cli, "ESCOLHEU BOLINHA DE QUEIJO :)")
        qtde = int(input("INFORME A QUANTIDADE: "))
        valor_bq = 0.85 * qtde
        print(f"O VALOR DE BOLINHA DE QUEIJO É R${valor_bq:.2f}")
    elif cod == 102:
        print(nome_cli, "ESCOLHEU KIBE :)")
        qtde = int(input("INFORME A QUANTIDADE: "))
        valor_kibe = 0.95 * qtde
        print(f"O VALOR DE {qtde} DE KIBE É R${valor_kibe:.2f}")
    elif cod == 103:
        print(nome_cli, "ESCOLHEU ESFIRRA DE CARNE :)")
        qtde = int(input("INFORME A QUANTIDADE: "))
        valor_ec = 0.95 * qtde
        print(f"O VALOR DA ESFIRRA DE CARNE É R${valor_ec:.2f}")
    elif cod == 104:
        print(nome_cli, "ESCOLHEU LANCHE NATURAL :)")
        qtde = int(input("INFORME A QUANTIDADE: "))
        valor_ln = 8.00 * qtde
        print(f"O VALOR DO LANCHE NATURAL É R${valor_ln:.2f}")
    elif cod == 105:
        print(nome_cli, "ESCOLHEU BEIRUTE :)")
        qtde = int(input("INFORME A QUANTIDADE: "))
        valor_br = 15.00 * qtde
        print(f"O VALOR DO BEIRUTE É R${valor_br:.2f}")
    elif cod == 106:
        print(nome_cli, "ESCOLHEU REFRIGERANTE :)")
        qtde = int(input("INFORME A QUANTIDADE: "))
        valor_rf = 5.50 * qtde
        print(f"O VALOR DO REFRIGERANTE É R${valor_rf:.2f}")
    else:
        print("CODIGO DE PRODUTO INVÁLIDO!")
        
    print(" ")
    status_pedido = input("CONTINUAR PEDIDO(S/N): ")
    total = valor_cf + valor_bq + valor_kibe + valor_ec + valor_ln + valor_br + valor_rf

print(" ")
print(f" TOTAL DO PEDIDO {pedido} DE {nome_cli} É DE: R${total:.2f}")
print (" VOLTE SEMPRE!!")
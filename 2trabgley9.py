# Questão 9: Exibir o dia da semana correspondente ao número
def dia_da_semana():
    numero = int(input("Digite um número de 1 a 7: "))
    dias = {
        1: "Domingo",
        2: "Segunda-Feira",
        3: "Terça-Feira",
        4: "Quarta-Feira",
        5: "Quinta-Feira",
        6: "Sexta-Feira",
        7: "Sábado"
    }
    
    if numero in dias:
        print(f"O dia correspondente é {dias[numero]}.")
    else:
        print("Número inválido. Digite um valor entre 1 e 7.")

dia_da_semana()

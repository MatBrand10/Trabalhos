# Questão 8: Exibir saudação com base na hora
def saudacao():
    nome = input("Digite seu nome: ")
    hora = int(input("Digite a hora atual (0-23): "))
    
    if 6 <= hora <= 12:
        print(f"Bom dia, {nome}!")
    elif 13 <= hora <= 17:
        print(f"Boa tarde, {nome}!")
    elif 18 <= hora <= 23:
        print(f"Boa noite, {nome}!")
    elif 0 <= hora <= 5:
        print(f"Durma bem, {nome}!")
    else:
        print("Hora inválida.")

saudacao()
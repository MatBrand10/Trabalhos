# Questão 6: Verificar se o usuário está apto a votar
def verificar_voto():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    if idade < 16:
        print(f"{nome}, você não pode votar.")
    elif 16 <= idade < 18 or idade > 70:
        print(f"{nome}, seu voto é facultativo.")
    else:
        print(f"{nome}, seu voto é obrigatório.")

verificar_voto()
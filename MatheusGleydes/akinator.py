import random

numero_secreto = random.randint(1,100)

tentativas = 0

print("Bem-vindo ao jogo de adivinhação ! tente adivinhar o número secreto entre 1 e 100.")

while True:
    tentativa = int(input("Digite sua tentativa: "))
    tentativas += 1
    
    if tentativa == numero_secreto:
        print(F"Parabens! Voce acertou o numero secreto {numero_secreto} em  {tentativas} tentativas.")
        break
    elif tentativa < numero_secreto:
        print("tente um numero maior.")
    else:
        print("tente um numero menor")
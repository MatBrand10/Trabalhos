numeros = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    numeros[x] = int(input("Digite 5 numeros, numero %d:" % ( x + 1)))
    x += 1
while True:
    escolhido = int(input("que posição você quer imprimir 1, 2, 3, 4 ou  5 (tecle 0 para sair):"))
    
    if escolhido == 0:
        break
    print ("Você escolheu o numero %d" % (numeros[escolhido - 1]))
    
    
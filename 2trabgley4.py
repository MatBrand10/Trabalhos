# Questão 4: Verificar se a senha atende aos critérios
def verificar_senha():
    import re
    senha = input("Digite uma senha: ")
    
    if (len(senha) >= 8 and
        re.search("[A-Z]", senha) and
        re.search("[a-z]", senha) and
        re.search("[0-9]", senha) and
        re.search("[!@#$%^&*]", senha)):
        print("Senha válida.")
    else:
        print("Senha inválida. Certifique-se de que ela contém pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula, um número e um caractere especial (!@#$%^&*).")

verificar_senha()

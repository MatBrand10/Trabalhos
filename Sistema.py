import os

#arquvo para armazenar os usuarios
ARQUIVO_USUARIOS = 'usuario.txt'

#Função para carregar os usuarios do arquivo
def carregar_usuarios():
    usuarios = {}
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'r') as arquivo:
            for linha in arquivo:
                login, senha = linha.strip().split(';')
                usuarios[login] = senha
    return usuarios

# Função para salvar os usuarios  no arquivo
def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, 'w')as arquivo:
        for login, senha in usuarios.items():
            arquivo.write(f'{login};{senha}\n')

# Função para cadastrar novo usuario
def cadastrar_usuario(usuarios):
    login = input('Digite um nome de usuário: ').strip()
    if login in usuarios:
        print('Usuário já existe. Tente outro.')
        return
    senha = input('Digite uma senha:').strip()
    usuarios[login]= senha
    salvar_usuarios(usuarios)
    print('Usuário cadastrado com sucesso!')

# Função para fazer login
def fazer_login(usuarios):
    login = input('Usuário:').strip()
    senha = input('Senha:').strip()
    if usuarios.get(login) == senha:
        print('Login realizado com sucesso!')
    else:
        print('Usuario ou senha incorretos.')

# Menu Principal
def menu():
    usuarios = carregar_usuarios()
    while True:
        print('\n--- Menu ---')
        print('1. Cadastrar usuário')
        print('2. Fazer login')
        print('3. Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_usuario(usuarios)
        elif opcao == '2':
            fazer_login(usuarios)
        elif opcao == '3':
            print('Saindo...')
            break
        else:
            print('Opção inválida. tente novamente.')

# Executar menu
menu()
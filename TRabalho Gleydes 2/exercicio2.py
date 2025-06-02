contatos = {
    "José Carlos": "jcarlos@gmail.com",
    "Dayse Melo": "dmelo@terra.com.br",
    "Ana Silva": "asilva@hotmail.com",
    "Fábio Moura": "fmoura@gmail.com",
    "Ivan Klouse": "Iklouse@ig.com.br",
    "Luísa Fontoura": "Lfontoura@bol.com.br"
}
nome_busca = input("Digite o nome do contato a ser buscado: ")
email = contatos.get(nome_busca)
if email:
    print(f"E-mail do contato {nome_busca}: {email}")
else:
    print("Contato não encontrado.")
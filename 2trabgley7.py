# Questão 7: Verificar categoria da habilitação
def verificar_habilitacao():
    nome = input("Digite seu nome: ")
    categoria = input("Digite a categoria da sua habilitação (A, B, C, D, E): ").upper()
    
    categorias = {
        "A": "Motocicletas",
        "B": "Carros de passeio",
        "C": "Veículos de carga acima de 3.500 kg",
        "D": "Ônibus e micro-ônibus",
        "E": "Veículos com unidade acoplada acima de 6.000 kg"
    }
    
    if categoria in categorias:
        print(f"{nome}, você pode dirigir: {categorias[categoria]}.")
    else:
        print("Categoria inválida.")

verificar_habilitacao()

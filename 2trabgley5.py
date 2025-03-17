# Questão 5: Verificar se uma data é válida
def verificar_data():
    from datetime import datetime
    data = input("Digite uma data no formato dd/mm/aaaa: ")
    try:
        datetime.strptime(data, "%d/%m/%Y")
        print("A data é válida.")
    except ValueError:
        print("A data é inválida.")

verificar_data()

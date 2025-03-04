# 09 - Cálculo de salário líquido
salarios_base = {"Analista Desenvolvedor Web": 4500, "Analista de Suporte": 3200, "Gerente de TI": 12299}
descontos = 0.07
bonus = {"Analista Desenvolvedor Web": 0.05, "Analista de Suporte": 0.04, "Gerente de TI": 0.10}
print("Salários líquidos:")
for cargo, salario_base in salarios_base.items():
    salario_final = (salario_base * (1 + bonus[cargo])) * (1 - descontos)
    print(f"{cargo}: R$ {salario_final:.2f}")

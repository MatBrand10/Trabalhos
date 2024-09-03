import json 

# Dados em formato JSON (simplificado para exemplo)
data = '''
[
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722},
    {"dia": 11, "valor": 0.0},
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 3847.4823},
    {"dia": 14, "valor": 373.7838},
    {"dia": 15, "valor": 2659.7563},
    {"dia": 16, "valor": 48924.2448},
    {"dia": 17, "valor": 18419.2614},
    {"dia": 18, "valor": 0.0},
    {"dia": 19, "valor": 0.0},
    {"dia": 20, "valor": 35240.1826},
    {"dia": 21, "valor": 43829.1667},
    {"dia": 22, "valor": 18235.6852},
    {"dia": 23, "valor": 4355.0662},
    {"dia": 24, "valor": 13327.1025},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
    {"dia": 27, "valor": 25681.8318},
    {"dia": 28, "valor": 1718.1221},
    {"dia": 29, "valor": 13220.495},
    {"dia": 30, "valor": 8414.61}
]
'''
 # Carregar os dados do JSON
faturamento = json.loads(data)

# Inicializar variáveis para cálculos
valores = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)

# Contar dias com faturamento superior à média
dias_acima_da_media = len([valor for valor in valores if valor > media_mensal])

# Exibir resultados
print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
# Faturamento por estado
faturamento_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcular o faturamento total
total_faturamento = sum(faturamento_estado.values())

# Calcular e exibir o percentual de representação
for estado, valor in faturamento_estado.items():
    percentual = (valor / total_faturamento) * 100
    print(f"Percentual de {estado}: {percentual:.2f}%")
def inverter_string(s):
    s_invertida = ""
    for char in s:
        s_invertida = char + s_invertida
    return s_invertida

# Testar a função
entrada = "Exemplo de string"
print(f"String original: {entrada}")
print(f"String invertida: {inverter_string(entrada)}")
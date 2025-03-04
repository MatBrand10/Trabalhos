# 08 - Cálculo de tempo de deslocamento
distancia_m = 5  # metros
velocidade_kmh = 10  # km/h
velocidade_ms = velocidade_kmh * 1000 / 3600  # Convertendo para m/s
tempo_s = distancia_m / velocidade_ms
print(f"O tempo para percorrer {distancia_m} metros a {velocidade_kmh} km/h é de {tempo_s:.2f} segundos.")

# 12 - Múltiplos e submúltiplos do metro
metros = float(input("Digite um valor em metros: "))
print(f"Múltiplos: km={metros/1000}, hm={metros/100}, dam={metros/10}, hectômetro={metros/100}, decâmetro={metros/10}")
print(f"Submúltiplos: dm={metros*10}, cm={metros*100}, mm={metros*1000}, micrômetro={metros*1e6}, nanômetro={metros*1e9}")

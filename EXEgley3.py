# 03 - Resolução de equações do 2º grau
def resolver_equacao(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Sem raízes reais"
    elif delta == 0:
        x = -b / (2*a)
        return f"Raiz única: {x:.2f}"
    else:
        x1 = (-b + (delta)) / (2*a)
        x2 = (-b - (delta)) / (2*a)
        return f"Raízes: {x1:.2f}, {x2:.2f}"

equacoes = [(3, -14, 8), (7, 5, -13), (13, -6, 1), (15, 2, -4)]
for a, b, c in equacoes:
    resultado = resolver_equacao(a, b, c)
    print(f"Equação {a}x² + {b}x + {c} = 0 → {resultado}")

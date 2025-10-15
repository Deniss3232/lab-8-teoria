"""
Problema 3 – Implementación y ANÁLISIS (Parte A)
-----------------------------------------------

Código base (idea):
for i in range(1, n//3 + 1):
    for j in range(1, n + 1, 4):
        # operación clave (print / contador++)

Conteo de iteraciones:
1) Bucle externo (i):
   i = 1 .. n//3  →  aproximadamente n/3 iteraciones  →  O(n).

2) Bucle interno (j):
   j = 1 .. n en pasos de 4  →  aproximadamente n/4 iteraciones  →  O(n).

3) Bucles anidados:
   Total ≈ (n/3) * (n/4) = n^2 / 12.  En notación asintótica (ignorando constantes):
   COMPLEJIDAD FINAL: O(n^2).

Conclusión:
La gráfica n vs tiempo (escala log–log) debe mostrar una pendiente cercana a 2,
coherente con crecimiento cuadrático.
"""

def funcion_p3(n: int) -> int:
    if n <= 0:
        return 0
    contador = 0
    limite_i = n // 3
    for _ in range(1, limite_i + 1):
        for _ in range(1, n + 1, 4):
            contador += 1  # operación clave
    return contador


# Prueba rápida manual
if __name__ == "__main__":
    for prueba in [4, 12, 24]:
        print(f"p3 n={prueba} -> ops={funcion_p3(prueba)}")

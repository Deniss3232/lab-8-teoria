"""
Problema 2
---------
Estructura típica (según enunciado interpretado):
for i in 1..n:
    for j in 1..n:
        print("*")
        break

La presencia de 'break' hace que el bucle interno se ejecute solo 1 vez por cada i.
Por lo tanto, el número de operaciones "clave" (el print) es ≈ n.

Complejidad: O(n)
"""

def funcion_p2(n: int) -> int:
    if n <= 0:
        return 0

    contador = 0
    for _ in range(1, n + 1):
        # El inner loop produciría n iteraciones, pero se rompe en la primera
        for _ in range(1, n + 1):
            contador += 1  # emula el print como operación clave
            break
    return contador


# Prueba rápida manual
if __name__ == "__main__":
    for prueba in [1, 5, 10]:
        print(f"p2 n={prueba} -> ops={funcion_p2(prueba)}")

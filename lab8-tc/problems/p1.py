"""
Problema 1
---------
Estructura (según enunciado):
i = n/2 .. n
  j = 1 .. (n - n/2)          # equivalente a j <= n/2 si n es par
    k = 1; while k <= n:
        counter++              # operación "clave"
        k = k * 2              # duplica k

Complejidad teórica:
- i itera ≈ n/2 + 1 veces  -> O(n)
- j itera ≈ n/2  veces     -> O(n)
- k itera ≈ log2(n) veces  -> O(log n)
Total: O(n * n * log n) = O(n^2 log n)

Esta función devuelve el número de operaciones clave (counter).
"""

def funcion_p1(n: int) -> int:
    if n <= 0:
        return 0

    contador = 0
    i = n // 2
    while i <= n:
        j = 1
        limite_j = n - (n // 2)  # ≈ n/2
        while j <= limite_j:
            k = 1
            while k <= n:
                contador += 1      # operación clave
                k *= 2             # k = k * 2
            j += 1
        i += 1
    return contador


# Prueba rápida manual
if __name__ == "__main__":
    for prueba in [1, 4, 8, 16]:
        print(f"p1 n={prueba} -> ops={funcion_p1(prueba)}")

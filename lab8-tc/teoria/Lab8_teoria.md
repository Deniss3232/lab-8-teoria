# Laboratorio 8 – Informe de Teoría

**Autor:** <TU NOMBRE AQUÍ>  
**Curso:** Teoría de la Computación  
**Fecha:** <dd/mm/aaaa>

---


---

\
    ## Parte A – Complejidad de P1, P2 y P3 (con procedimiento)

    ### Problema 1
    **Estructura:**
    - `i = n/2 .. n`  →  ~O(n)  
    - `j = 1 .. n - n/2`  →  ~O(n)  
    - `k = 1, 2, 4, ... <= n`  →  O(log n)  

    **Total:** \( O(n \cdot n \cdot \log n) = O(n^2 \log n) \).

    ### Problema 2
    **Idea:** Bucle doble con `break` al iniciar el interno.
    - Externo: O(n)  
    - Interno: ejecuta 1 iteración por cada `i` → O(1)  

    **Total:** \( O(n) \).

    ### Problema 3 – Análisis paso a paso
    **Código base (idea):**
    ```python
    for i in range(1, n//3 + 1):
        for j in range(1, n + 1, 4):
            pass  # operación clave
    ```
    - **Bucle externo (`i`)**: recorre \( \lfloor n/3 \rfloor \approx n/3 \) → **O(n)**  
    - **Bucle interno (`j`)**: de 1 a n **en pasos de 4**: \( \lceil n/4 \rceil \approx n/4 \) → **O(n)**  
    - **Anidados**: \( (n/3) \cdot (n/4) = n^2/12 \) → **\( O(n^2) \)**

    **Conclusión:** La gráfica n vs. tiempo (escala log–log) debe mostrar tendencia cuadrática.


---

\
    ## Problema 4 – Mejor, Promedio y Peor caso

    ### Búsqueda lineal
    - **Mejor:** \(O(1)\) – el elemento está al inicio.  
    - **Promedio:** \(O(n)\) – en promedio ~n/2 comparaciones.  
    - **Peor:** \(O(n)\) – al final o no está.

    ### Búsqueda binaria (arreglo ordenado)
    - **Mejor:** \(O(1)\).  
    - **Promedio / Peor:** \(O(\log n)\) – se reduce a la mitad el espacio de búsqueda cada paso.

    ### Quicksort
    - **Mejor:** \(O(n\log n)\) – particiones balanceadas.  
    - **Promedio:** \(O(n\log n)\) – pivote razonablemente bueno en promedio.  
    - **Peor:** \(O(n^2)\) – pivotes muy desbalanceados (p. ej. entrada ordenada y pivote extremo).  

    *Notas:* la aleatorización del pivote reduce la probabilidad del peor caso; la búsqueda binaria
    requiere estrictamente datos ordenados.


---

## Problema 5 – Enunciados V/F con justificación

**1. (V)** Si f(n) = O(g(n)), entonces c·f(n) = O(g(n)) para cualquier c > 0.

Justificación: Multiplicar por constante positiva no cambia la clase asintótica.

**2. (F)** Si un algoritmo es O(n), siempre es más rápido que uno O(n^2).

Justificación: La notación es asintótica; para n pequeños y constantes grandes, O(n^2) puede ganar.

**3. (V)** Si f(n) = Θ(g(n)), entonces f(n) = O(g(n)) y f(n) = Ω(g(n)).

Justificación: Por definición de Θ, ambas cotas (superior e inferior) se cumplen.

**4. (F)** Búsqueda binaria funciona aunque el arreglo no esté ordenado.

Justificación: La búsqueda binaria requiere orden para dividir correctamente el espacio de búsqueda.

**5. (V)** Quicksort tiene peor caso O(n^2).

Justificación: Con pivotes muy desbalanceados (p. ej., arreglo ya ordenado y pivote extremo).

**6. (F)** Agregar una constante al tiempo de ejecución cambia la notación O grande.

Justificación: Las constantes aditivas no afectan la clase asintótica.


---

## Conclusiones
- **P1** mostró crecimiento coherente con \(O(n^2\log n)\), por lo que valores muy grandes de \(n\) se vuelven prohibitivos.
- **P2** fue prácticamente lineal \(O(n)\).
- **P3** evidenció crecimiento cuadrático \(O(n^2)\).
Estas tendencias se observan en las gráficas de tiempo vs. tamaño de entrada.


---

## Anexo – Gráficas de tiempo

### P1

![P1](analysis_out/p1_grafica.png)

### P2

![P2](analysis_out/p2_grafica.png)

### P3

![P3](analysis_out/p3_grafica.png)


---

## Referencias
- Cormen, Leiserson, Rivest, Stein. *Introduction to Algorithms*.
- Sedgewick & Wayne. *Algorithms*.
- Apuntes de clase.

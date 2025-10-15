# genera_teoria.py
from pathlib import Path
from textwrap import dedent

# === Personaliza estos datos ===
AUTOR = "<TU NOMBRE AQUÍ>"
CURSO = "Teoría de la Computación"
FECHA = "<dd/mm/aaaa>"

# === Enunciados de P5 (puedes editar/agregar) ===
# Formato: ("enunciado", "V" o "F", "justificación breve")
P5_ITEMS = [
    ("Si f(n) = O(g(n)), entonces c·f(n) = O(g(n)) para cualquier c > 0.", "V",
     "Multiplicar por constante positiva no cambia la clase asintótica."),
    ("Si un algoritmo es O(n), siempre es más rápido que uno O(n^2).", "F",
     "La notación es asintótica; para n pequeños y constantes grandes, O(n^2) puede ganar."),
    ("Si f(n) = Θ(g(n)), entonces f(n) = O(g(n)) y f(n) = Ω(g(n)).", "V",
     "Por definición de Θ, ambas cotas (superior e inferior) se cumplen."),
    ("Búsqueda binaria funciona aunque el arreglo no esté ordenado.", "F",
     "La búsqueda binaria requiere orden para dividir correctamente el espacio de búsqueda."),
    ("Quicksort tiene peor caso O(n^2).", "V",
     "Con pivotes muy desbalanceados (p. ej., arreglo ya ordenado y pivote extremo)."),
    ("Agregar una constante al tiempo de ejecución cambia la notación O grande.", "F",
     "Las constantes aditivas no afectan la clase asintótica."),
]

OUT_DIR = Path("teoria")
OUT_MD = OUT_DIR / "Lab8_teoria.md"
IMG_DIR = Path("analysis_out")  # donde guardaste las gráficas del profiling

def portada() -> str:
    return dedent(f"""\
    # Laboratorio 8 – Informe de Teoría

    **Autor:** {AUTOR}  
    **Curso:** {CURSO}  
    **Fecha:** {FECHA}

    ---
    """)

def parteA() -> str:
    return dedent(r"""\
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
    """)

def problema4() -> str:
    return dedent(r"""\
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
    """)

def problema5(items) -> str:
    lines = ["## Problema 5 – Enunciados V/F con justificación\n"]
    if not items:
        lines.append("- *(Agrega aquí tus enunciados y marca V/F con una justificación breve.)*")
    else:
        for i, (text, vf, why) in enumerate(items, 1):
            lines.append(f"**{i}. ({vf})** {text}\n\nJustificación: {why}\n")
    return "\n".join(lines)

def conclusiones() -> str:
    return dedent("""\
    ## Conclusiones
    - **P1** mostró crecimiento coherente con \(O(n^2\log n)\), por lo que valores muy grandes de \(n\) se vuelven prohibitivos.
    - **P2** fue prácticamente lineal \(O(n)\).
    - **P3** evidenció crecimiento cuadrático \(O(n^2)\).
    Estas tendencias se observan en las gráficas de tiempo vs. tamaño de entrada.
    """)

def referencias() -> str:
    return dedent("""\
    ## Referencias
    - Cormen, Leiserson, Rivest, Stein. *Introduction to Algorithms*.
    - Sedgewick & Wayne. *Algorithms*.
    - Apuntes de clase.
    """)

def anexar_graficas_si_existen() -> str:
    bloques = []
    mapping = [("P1", "p1_grafica.png"), ("P2", "p2_grafica.png"), ("P3", "p3_grafica.png")]
    existentes = []
    for titulo, fname in mapping:
        path = IMG_DIR / fname
        if path.exists():
            existentes.append(f"### {titulo}\n\n![{titulo}]({(IMG_DIR / fname).as_posix()})\n")
    if existentes:
        bloques.append("## Anexo – Gráficas de tiempo\n")
        bloques.extend(existentes)
    return "\n".join(bloques)

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    partes = [
        portada(),
        parteA(),
        problema4(),
        problema5(P5_ITEMS),
        conclusiones(),
        anexar_graficas_si_existen(),
        referencias(),
    ]
    OUT_MD.write_text("\n\n---\n\n".join(partes), encoding="utf-8")
    print(f"✔ Informe generado en: {OUT_MD.resolve()}")

if __name__ == "__main__":
    main()

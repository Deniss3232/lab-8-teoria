"""
Script de perfilado y gráficos para P1, P2 y P3.

- Mide tiempo de ejecución para una lista de tamaños n
- Guarda CSV con (n, tiempo_s)
- Genera PNG (una gráfica por problema)
"""
##para correr desde la raíz del proyecto:
## cd C:\Users\iqden\Desktop\lab8-tc
## python -m analysis.profile_all

import csv
import time
from pathlib import Path
import matplotlib.pyplot as plt

#  Importamos las tres funciones
from problems.p1 import funcion_p1
from problems.p2 import funcion_p2
from problems.p3 import funcion_p3

OUTDIR = Path("analysis_out")
OUTDIR.mkdir(exist_ok=True)

#  Solo hasta 10000 ya que con lo demas no corre
NVALS = [1, 10, 100, 1000, 10000]

def medir_tiempo(func, n):
    inicio = time.time()
    func(n)
    return time.time() - inicio

def perfilar(nombre, funcion):
    resultados = []
    for n in NVALS:
        t = medir_tiempo(funcion, n)
        resultados.append((n, t))
        print(f"{nombre} n={n}: {t:.6f}s")
    return resultados

def guardar_csv(nombre, resultados):
    archivo = OUTDIR / f"{nombre}_resultados.csv"
    with open(archivo, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "tiempo (s)"])
        writer.writerows(resultados)
    return archivo

def graficar(nombre, resultados):
    ns = [r[0] for r in resultados]
    tiempos = [r[1] for r in resultados]

    plt.figure()
    plt.plot(ns, tiempos, marker='o')
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (s)")
    plt.title(f"{nombre}: n vs tiempo")
    plt.grid(True)
    plt.savefig(OUTDIR / f"{nombre}_grafica.png", dpi=150, bbox_inches="tight")
    plt.close()

def main():
    #  P1
    r1 = perfilar("P1", funcion_p1)
    guardar_csv("p1", r1)
    graficar("P1", r1)

    # P2
    r2 = perfilar("P2", funcion_p2)
    guardar_csv("p2", r2)
    graficar("P2", r2)

    # P3
    r3 = perfilar("P3", funcion_p3)
    guardar_csv("p3", r3)
    graficar("P3", r3)

if __name__ == "__main__":
    main()


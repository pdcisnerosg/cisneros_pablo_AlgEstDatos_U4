import random
import time
from algoritmos import burbuja, merge_sort, busqueda_lineal, busqueda_binaria

tamanos = [1000, 2000, 4000, 8000]
repeticiones = 5
busquedas = 1000  # una búsqueda sola es tan rápida que el cronómetro ni la ve, por eso mido 1000 de una

def medir(funcion, datos):
    """Devuelve el tiempo en segundos que tarda funcion(datos)."""
    copia = list(datos)
    inicio = time.perf_counter()
    funcion(copia)
    return time.perf_counter() - inicio

# Busco el 0, que nunca está en los datos: así las dos búsquedas caen en el peor caso
def lineal(datos):
    for _ in range(busquedas):
        busqueda_lineal(datos, 0)

def binaria(datos):
    for _ in range(busquedas):
        busqueda_binaria(datos, 0)

# Antes de medir reviso que las cuatro funciones den bien el resultado
def comprobar():
    datos = [random.randint(1, 10**6) for _ in range(500)]
    ordenados = sorted(datos)
    assert burbuja(list(datos)) == ordenados
    assert merge_sort(list(datos)) == ordenados
    for x in datos[:50]:
        assert datos[busqueda_lineal(datos, x)] == x
        assert ordenados[busqueda_binaria(ordenados, x)] == x
    assert busqueda_lineal(datos, 0) == -1 and busqueda_binaria(ordenados, 0) == -1
    print("Los cuatro algoritmos funcionan bien (comparados con sorted())")

# R4 - Plantilla del enunciado, repetida para cada algoritmo
def tabla(nombre, funcion, datos_por_n, ordenar=False):
    print(f"\n{nombre}")
    print(f"{'n':>6} {'tiempo(s)':>12} {'razon':>8}")
    anterior = None
    for n in tamanos:
        datos = datos_por_n[n]
        if ordenar:
            datos = merge_sort(datos)  # la binaria necesita la lista ordenada; esto no entra en el tiempo
        # mido varias veces y me quedo con el menor, porque si la compu se distrae solo suma tiempo
        t = min(medir(funcion, datos) for _ in range(repeticiones))
        razon = f"{t/anterior:.2f}" if anterior else "-"
        print(f"{n:>6} {t:>12.5f} {razon:>8}")
        anterior = t

def main():
    comprobar()
    datos_por_n = {n: [random.randint(1, 10**6) for _ in range(n)] for n in tamanos}
    print(f"Se toma el menor de {repeticiones} tiempos por tamaño. La burbuja se demora unos segundos.")
    tabla("Burbuja O(n^2), razón esperada ~4", burbuja, datos_por_n)
    tabla("Merge Sort O(n log n), razón esperada algo más de 2", merge_sort, datos_por_n)
    tabla(f"Búsqueda lineal O(n), {busquedas} búsquedas, razón esperada ~2", lineal, datos_por_n)
    tabla(f"Búsqueda binaria O(log n), {busquedas} búsquedas, razón esperada apenas mayor que 1", binaria, datos_por_n, ordenar=True)

if __name__ == "__main__":
    main()

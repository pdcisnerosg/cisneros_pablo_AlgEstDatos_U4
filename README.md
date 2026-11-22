# Laboratorio de eficiencia

Programa en Python con dos ordenamientos y dos búsquedas. Mide cuánto se demora cada uno con listas de 1.000, 2.000, 4.000 y 8.000 números y saca la razón entre cada medición y la anterior, para ver si cuadra con lo que dice la teoría.

Autor: Pablo Cisneros. Materia: Algoritmos y Estructuras de Datos (Ciencia de Datos).

## Cómo ejecutar

Necesita Python 3 y nada más: solo usa `random` y `time`, que ya vienen con Python.

```
python main.py
```

En Mac, si `python` no funciona, usa `python3 main.py`. En mi Mac se demora unos 10 segundos, casi todo por la burbuja con 8.000 números.

## Archivos

| Archivo | Qué tiene |
|---|---|
| `algoritmos.py` | Burbuja, Merge Sort, búsqueda lineal y búsqueda binaria |
| `main.py` | La revisión de los algoritmos y la medición de tiempos con la plantilla del enunciado |

## Algoritmos que se comparan

| Requerimiento | Algoritmo | Tiempo | Espacio | Razón esperada al duplicar n |
|---|---|---|---|---|
| R2 | Burbuja | O(n^2) | O(1) | ~4 |
| R2 | Merge Sort | O(n log n) | O(n) | algo más de 2 |
| R3 | Búsqueda lineal | O(n) | O(1) | ~2 |
| R3 | Búsqueda binaria | O(log n) | O(1) | apenas mayor que 1 |

La búsqueda binaria trabaja sobre la lista que deja ordenada Merge Sort. Ese ordenamiento se hace antes y no entra en el tiempo medido.

## Cómo se mide (R4)

- Antes de medir, `comprobar()` revisa que los dos ordenamientos den lo mismo que `sorted()` y que las dos búsquedas encuentren cada número.
- Las listas de 1.000, 2.000, 4.000 y 8.000 números se generan al azar, y los cuatro algoritmos usan las mismas.
- `medir()` es la función de la plantilla del enunciado, con `time.perf_counter()`.
- Cada tamaño se mide 5 veces y me quedo con el tiempo menor. Si la compu se distrae con otro programa eso solo suma tiempo, así que el menor es la medición más limpia.
- Una búsqueda sola dura microsegundos y el cronómetro casi no la ve. Por eso cada medición de búsqueda hace 1.000 búsquedas del número 0, que nunca está en la lista: ese es el peor caso de las dos.
- En pantalla sale una tabla por algoritmo con `n`, el tiempo en segundos y la razón con la medición anterior.

## Resultados en mi Mac

Corrida del 17 de noviembre de 2026 (Python 3.14). Los segundos cambian en cada computador; lo que hay que mirar son las razones.

| n | Burbuja (s) | razón | Merge Sort (s) | razón | Lineal (s) | razón | Binaria (s) | razón |
|---|---|---|---|---|---|---|---|---|
| 1000 | 0.01757 | - | 0.00087 | - | 0.01490 | - | 0.00052 | - |
| 2000 | 0.07260 | 4.13 | 0.00203 | 2.32 | 0.02970 | 1.99 | 0.00060 | 1.16 |
| 4000 | 0.30746 | 4.24 | 0.00421 | 2.07 | 0.06051 | 2.04 | 0.00067 | 1.11 |
| 8000 | 1.23283 | 4.01 | 0.00860 | 2.04 | 0.12129 | 2.00 | 0.00072 | 1.07 |
| teoría | | ~4 | | ~2,2 | | ~2 | | ~1,1 |

La burbuja, la lineal y la binaria cuadran con la teoría. Merge Sort se cumple a medias: está sobre 2, pero las dos últimas razones quedaron debajo de 2,2. En otra corrida del 22 de noviembre Merge Sort dio 2.06, 1.83 y 1.97, mientras la burbuja y la lineal casi no cambiaron. Cuando una medición dura pocos milisegundos la razón baila bastante. La explicación completa está en el informe.

## Profiling con cProfile

```
python -m cProfile -s tottime main.py
```

Primeras líneas del reporte en una corrida de prueba:

```
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       21   13.324    0.634   13.324    0.634 algoritmos.py:3(burbuja)
    20051    1.535    0.000    1.535    0.000 algoritmos.py:39(busqueda_lineal)
    90475    0.399    0.000    0.638    0.000 algoritmos.py:26(fusionar)
```

El cuello de botella es `burbuja`: se llama 21 veces y se lleva 13,3 de los 15,7 segundos del programa, más o menos el 85 %. La búsqueda binaria se llamó 20.051 veces y casi ni suma tiempo.

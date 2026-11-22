# R2 - Ordenamiento simple
# burbuja: O(n^2) tiempo, O(1) espacio
def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        hubo_cambio = False
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_cambio = True
        if not hubo_cambio:  # si en una pasada no se cambió nada, ya está ordenada
            break
    return lista

# R2 - Ordenamiento eficiente
# merge_sort: O(n log n) tiempo, O(n) espacio
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izq = merge_sort(lista[:medio])
    der = merge_sort(lista[medio:])
    return fusionar(izq, der)

# fusionar: O(n)
def fusionar(a, b):
    resultado, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1
    return resultado + a[i:] + b[j:]

# R3 - Búsqueda lineal
# busqueda_lineal: O(n) tiempo, O(1) espacio
def busqueda_lineal(lista, objetivo):
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i
    return -1

# R3 - Búsqueda binaria (ojo: la lista tiene que estar ordenada)
# busqueda_binaria: O(log n) tiempo, O(1) espacio
def busqueda_binaria(lista, objetivo):
    izq, der = 0, len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1
    return -1

#!/usr/bin/python3

"""
Modulo con una funcion para ordenar un arreglo de 20 enteros ascendentemente
"""


def print_sort(arr, n):
    """
    Imprime el array ordenado
    """
    for i in range(n):
        print(arr[i])


def sort_asc(arr=[]):
    """Esta funcion ordena ascendentemente una lista de enteros """
    if arr is None:
        return
    # Para ordenar es necesario saber la longitud de nuestro array
    n = len(arr)
    # Metodo de Ordenamiento mas rápido para ordenar arreglos
    quick_sort(arr, 0, n-1)
    # Metodo para imprimir y verificar el orden del arreglo
    print_sort(arr, n)


def quick_sort(arr, low, high):
    """Metodo que ejecuta el ordenamiento del array"""
    if len(arr) == 1:
        return arr
    if low < high:
        # particionamos el indice, para ordenar el numero
        pi = partition(arr, low, high)
        # Separadamente ordenamos los elementos antes y despues de la particion
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    """
    Esta funcion toma el ultimo elemento como pivot, y posiciona este elemento
    en su posicion correcta dentro del array, y ubica todos los elementos
    menores al pivot a su izquierda y los elementos mayores a su derecha
    """
    i = (low-1)         # Index del elemento mas pequeño.
    pivot = arr[high]     # pivot - el ultimo elemento del array

    for j in range(low, high):

        # Si el elemento actual is mas pequeño o igual al pivot
        if arr[j] <= pivot:

            # Incrementa el index del elemento mas pequeño
            i = i+1
            # Genero un swap en el siguiente indice del elemento mas
            # pequeño y el actual.
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


if __name__ == "__main__":
    arr = [
        19, 20, 4, 7, 9, 12, 1, 3, 5, 8, 6, 10, 2, 11, 14, 13, 15, 16, 18, 17
    ]
    sort_asc(arr)

#!/usr/bin/python3

"""Modulo para ejecutar funcion de ordenamiento de array"""


def bubble_sort(lst):
    """Ordena linealmente un array """
    if (lst is None):
        return []
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

if __name__ == '__main__':
    arr = [
        19, 20, 4, 7, 9, 12, 1, 3, 5, 8, 6, 10, 2, 11, 14, 13, 15, 16, 18, 17
    ]
    print(bubble_sort(arr))

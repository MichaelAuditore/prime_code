#!/usr/bin/python3
"""
Modulo con una funcion que permite imprimir todas las
permutaciones entre 1 y un digito dado
"""


def permutation(my_lst):
    """ Obtiene todas las permutaciones de una lista dada """

    # Si solo hay un item retorna la unica permutacion posible
    if len(my_lst) == 1:
        return [my_lst]

    # Encuentra todas las permutaciones del arreglo dado
    # si hay mas de un numero

    # lista vacia para alojar las permutaciones resultantes
    l = []

    # Itera cada elemento y genera las permutaciones posibles por cada uno
    for i in range(len(my_lst)):
        m = my_lst[i]

        # Extrae el elemento m de la lista
        # rem: lista resultante de la extracion del elemento m
        rem = my_lst[:i] + my_lst[i+1:]

        # Genera recursivamente todas las permutaciones donde
        # el elemento m es primero
        for p in permutation(rem):
            # append a la lista vacia, cuando encuentra una permutacion
            l.append([m] + p)
    return l


def print_permutations(perm):
    """imprime las permutaciones como str"""

    for p in perm:
        if p is not perm[len(perm) - 1]:
            print(''.join([str(n) for n in p]), end=",")
        else:
            print(''.join([str(n) for n in p]))


def get_permutations(number):
    """ Metodo que obtiene todas las permutaciones posibles entre 1
    y el numero ingresado.
    """
    if number > 0 and number < 10:
        my_list = [i for i in range(1, number + 1)]
        permutations = permutation(my_list)
        print_permutations(permutations)
    else:
        print("Ingrese un numero entre 1 y 9")

if __name__ == "__main__":
    get_permutations(4)

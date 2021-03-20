#!/usr/bin/python3

import itertools
"""
Modulo con una funcion que permite imprimir todas las
permutaciones entre 1 y un digito dado
"""


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
        permutations = list(itertools.permutations(my_list, len(my_list)))
        print_permutations(permutations)

    else:
        print("Ingrese un numero entre 1 y 9")

if __name__ == "__main__":
    get_permutations(4)

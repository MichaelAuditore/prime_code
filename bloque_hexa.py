#!/usr/bin/python3
"""Modulo para identificar una trama hexadecimal"""


def convertir_a_binario(bloque, scale=16, num_bits=16):
    """Convierte un bloque hexadecimal a un binario de 16 bits """

    # Convierto a binario y elimino el primer bit perteneciente al encendido
    # o apagado
    binario = (bin(int(bloque, scale)).lstrip("0b").zfill(num_bits))
    leds = binario[1:8]
    pulso = binario[8:16]

    return {'leds': leds, 'pulso': pulso}


def convertir_a_int(data):
    """ Convierte los valores de un objeto en entero y los imprime """
    data["leds"] = int(data["leds"], 2)
    data["pulso"] = int(data["pulso"], 2)
    imprimir_data(data)


def imprimir_data(data):
    """Imprime los datos correspondientes a cada bloque """
    print("Número de leds: ", data["leds"])
    print("Valor de pulso: ", data["pulso"])


def evaluar_trama(trama):
    """
    Recorre una trama hexadecimal en busca de los datos
    numero de leds y valor de pulso.
    de izq - der (+ significativo a - significativo)
    """
    bloques = trama.split()
    for bloque in bloques:
        print("Bloque a evaluar", bloque)
        data = convertir_a_binario(bloque)
        convertir_a_int(data)


if __name__ == "__main__":
    trama = "58A6 FC89 BD1A 4313 1250 0F21 C89B D1A4"
    evaluar_trama(trama)

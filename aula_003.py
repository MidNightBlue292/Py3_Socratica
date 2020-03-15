from math import pi


# help(volume_esfera)
def volume_esfera(r):
    """
    volume da esfera
    :param r:
    raio da esfera
    :return:
    devolve o volume
    """
    v_esfera = (4.0 / 3.0) * pi * r**3
    return v_esfera


# help(volume_triangulo)
def volume_triangulo(b, h):
    """
    volume do triangulo
    :param b:
    tamanho da base
    :param h:
    tamanho da altura
    :return:
    devolve o volume
    """
    v_triangulo = 0.5 * b * h
    return v_triangulo


def cm(feet=0, inches = 0):
    """
    converte tamanho para pés e polegadas
    :param feet:
    calcula pés em cm
    :param inches:
    calcula polegadas em cm
    :return:
    devolve a soma dos 2 valores
    """
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm


def g(x, y=0):
    return x + y


print(f'Volume da esfera com um raio de 2 = {volume_esfera(2)}')
print(f'Volume do triângulo de base 3 e altura 6 = {volume_triangulo(3, 6)}')
print()
print(cm(feet=5))
print(cm(inches=70))
print(cm(feet=5, inches=8))
print(cm(inches=8, feet=5))
print()
print(g(5))

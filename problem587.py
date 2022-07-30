from math import *


l = 1 - 0.25 * pi


def intersection(n):
    y = (n + 1 - (2 * n) ** 0.5) / (n ** 2 + 1)
    return y * n, y


def weird(x, y):
    trapeze = (1 + y) * (1 - x) / 2
    circle_part = pi * asin(1 - x) / (2 * pi)
    return trapeze - circle_part


def concave(n):
    x, y = intersection(n)
    triangle = x * y / 2
    area = triangle + weird(x, y)
    return area


def percentage(n):
    return concave(n) / l


def first(perc):
    i = 1
    while percentage(i) > perc:
        i += 1
    return i

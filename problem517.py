import math


def gen_primes(m, n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(math.ceil(n ** 0.5)):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(m + 1, n) if primes[i]]


def g(a, x):
    if x < a:
        return 1
    else:
        return g(a, x - 1) + g(a, x - a)


def g2(n):
    return g(n ** 0.5, n)

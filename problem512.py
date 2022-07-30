import math


def gen_primes(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(math.ceil(n ** 0.5)):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]


def gen_totient(n):
    n = n + 1
    totient = [0] * n
    totient[1] = 1
    primes = gen_primes(n)
    for p in primes:
        totient[p] = p - 1
        for i in range(math.ceil(n / p)):
            if totient[i] != 0:
                if i % p == 0:
                    totient[p * i] = totient[i] * p
                else:
                    totient[p * i] = totient[i] * (p - 1)
    return totient


phi = gen_totient(5 * 10 ** 8)
print("got totients")


def f(n):
    if n % 2 == 0:
        return 0
    else:
        return phi[n]


def g(n):
    return sum([f(i) for i in range(1, n + 1)])


ans = g(5 * 10 ** 8)
print(ans)

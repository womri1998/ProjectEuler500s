from math import ceil, gcd


def gen_primes(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(ceil(n ** 0.5)):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]


def phi(n, i):
    if n == 1:
        return 1
    x = n - 1
    res = 1
    while n - 1 == x and i != len(primes):
        if n % primes[i] == 0:
            res *= primes[i] - 1
            n //= primes[i]
        while n % primes[i] == 0:
            res *= primes[i]
            n //= primes[i]
        i += 1
    return res * phi(n, i) if n - 1 != x else x


primes = gen_primes(int(1006000 ** 0.5))
phis = [phi(i, 0) for i in range(10 ** 6, 10 ** 6 + 5000)]


def primality_check(n):  # assuming list of primes named "primes" exists
    for p in primes:
        if p ** 2 >= n:
            return True
        if n % p == 0:
            return False


def euclid(n, m):
    if n < m:
        n, m = m, n
    x, y = (n, 1, 0), (m, 0, 1)
    while y[0] != 0:
        k = x[0] // y[0]
        x, y = y, (x[0] % y[0], x[1] - k * y[1], x[2] - k * y[2])
    return x


def g(a, n, b, m):
    a, b = a % n, b % m
    c = gcd(n, m)
    if a % c != b % c:
        return 0
    else:
        res = a % c
        a2, b2 = (a - res) // c, (b - res) // c
        a3, b3 = euclid(n, m)[1:]
        res += a3 * a2 * m + b3 * b2 * n
        lcm = n * m // c
        return res % lcm


def result():
    total = 0
    for i in range(10 ** 6, 10 ** 6 + 5000):
        print(i - 10 ** 6)
        for j in range(i + 1, 10 ** 6 + 5000):
            total += g(phis[i - 10 ** 6], i, phis[j - 10 ** 6], j)
    return total

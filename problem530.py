import math


def f(n):
    res = 0
    for i in range(1, n + 1):
        if n % i == 0:
            res += math.gcd(i, n // i)
    return res


def F(n):
    return sum([f(i) for i in range(1, n + 1)])

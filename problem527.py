from fractions import Fraction


def binary_search(a, n): # assume a is sorted in ascending order
    l, h, count = 0, len(a) - 1, 0
    while l <= h:
        count += 1
        m = (l + h) // 2
        if a[m] == n:
            return count
        elif a[m] > n:
            h = m - 1
        else:
            l = m + 1
    return -1


def b(n):
    i = 0
    total = 0
    m = n
    while m != 0:
        if 2 ** i > m:
            total += i * m
            m = 0
        else:
            total += i * 2 ** i
            m -= 2 ** i
        i += 1
    return Fraction(total, n) + 1


was = [0, 1]


def next(n):
    expected = 0
    for i in range(n):
        expected += i * was[i]
    expected *= Fraction(2, n ** 2)
    return expected + 1


def next(n):
    return was[n - 1] * (1 - Fraction(1, n ** 2)) + Fraction(2 * n - 1, n ** 2)

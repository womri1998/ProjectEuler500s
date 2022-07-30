from math import ceil, gcd


was = []
for i in range(101):
    was.append([-1] * 101)
perfect_squares = [i ** 2 for i in range(141)]


def square(a, b, c, d):
    return square_points(a, b, c, d) in perfect_squares


def squares(n):
    res = 0
    for a in range(1, n + 1):
        print(a)
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                for d in range(1, n + 1):
                    res += square(a, b, c, d)
    return res


def square_points(a, b, c, d):
    return ((a + c) * (b + d) + 2 - line_points(a, b, c, d)) // 2


def line_points(a, b, c, d):
    return gcd(a, b) + gcd(b, c) + gcd(c, d) + gcd(d, a)

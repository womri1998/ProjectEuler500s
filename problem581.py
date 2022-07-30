primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def smooth(n):
    for p in primes:
        while n % p == 0:
            n //= p
    return True if n == 1 else False


def triangular(n):
    return n * (n + 1) // 2


def check():
    i = 1
    tot = 0
    while True:
        if smooth(triangular(i)):
            tot += i
            print(i, tot)
        i += 1

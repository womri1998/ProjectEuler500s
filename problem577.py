def nc2(n):
    return n * (n - 1) // 2


def h(n):
    res = 0
    while n > 2:
        res += nc2(n - 1)
        n -= 3
    return res

def seq(n):
    if n % 6 == 0:
        return 1
    elif n % 6 == 3:
        return 4
    elif n % 6 in (1, 5):
        return 2
    else:
        return 3


def to_int(arr):
    arr = arr[::-1]
    res = 0
    for i in range(len(arr)):
        res += arr[i] * 10 ** i
    return res


def next(n, m): # n = steps done in 1st sequence, m = sum needed
    res = []
    while m > 0:
        x = seq(n)
        m -= x
        res.append(x)
        n += 1
    return to_int(res), n


def gen_seq(n):
    i = 0
    a = []
    for j in range(1, n + 1):
        x, i = next(i, j)
        a.append(x)
    return a

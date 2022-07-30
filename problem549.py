def gen_primes(n):
    done = 0
    p_powers = []
    while n != 0:
        suspects = [[True, 0]] * min(n, 10 ** 6)
        n -= min(n, 10 ** 6)
        if done == 0:
            suspects[0], suspects[1] = [False, 0], [False, 0]
        for p in p_powers:
            r = 0 if done % p == 0 else p - done % p
            m = ((r + done) // p) % p
            small = p_power_smallest(p[0], p[1])
            for i in range(r, len(suspects), p):
                if m != 0:
                    suspects[i] = False
                suspects[i][1] = max(suspects[i][1], small)
        for i in range(len(suspects)):
            if suspects[i][0]:
                for j in range(2 * i + done, len(suspects), i + done):
                    suspects[j][0] = False
        p_powers += [(i + done, suspects[i][1]) for i in range(len(suspects)) if suspects[i][0]]
        done += 10 ** 6
        print(done)
    return p_powers


def p_power(n, p):
    while n % p == 0:
        n //= p
    return True if n == 1 else False


def p_power_smallest(n, p): # assuming there exists an integer m s.t. p ** m == n
    i = 0
    while n != 1 and n != 0:
        i += p
        j = i
        while j % p == 0:
            j //= p
            n //= p
    return i


def gen_primes(n):
    done = 0
    primes = []
    while n != 0:
        if n < 10 ** 6:
            suspects = [True] * n
            n = 0
        else:
            suspects = [True] * 10 ** 6
            n -= 10 ** 6
        if done == 0:
            suspects[0], suspects[1] = False, False
        for p in primes:
            r = 0 if done % p == 0 else p - done % p
            for i in range(r, len(suspects), p):
                suspects[i] = False
        for i in range(len(suspects)):
            if suspects[i]:
                for j in range(2 * i + done, len(suspects), i + done):
                    suspects[j] = False
        primes += [i + done for i in range(len(suspects)) if suspects[i]]
        done += 10 ** 6
        print(done)
    return primes


def smallest_sum(n):
    #primes = gen_primes(n)
    tot, done = 0, 0
    while n != 0:
        if n < 10 ** 6:
            smallest = [0] * n
            n = 0
        else:
            smallest = [0] * 10 ** 6
            n -= 10
        for p in primes:
            if p > done + 10 ** 6:
                break
            k = 1
            while p ** k < done + 10 ** 6:
                r = 0 if done % p ** k == 0 else p ** k - done % p ** k
                for i in range(r, len(smallest), p ** k):
                    smallest[i] = max(smallest[i], p_power_smallest(p ** k, p))
                k += 1
        tot += sum(smallest)
        done += 10 ** 6
        print(done)
    return tot

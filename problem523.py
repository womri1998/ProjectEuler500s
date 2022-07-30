def sort(a):
    count = 0
    sorted = False
    while not sorted:
        found = False
        i = 0
        while not found and i < len(a) - 1:
            if a[i] > a[i + 1]:
                found = True
            i += 1
        if found:
            count += 1
            a = [a[i]] + a[:i] + a[i + 1:]
            print(a)
        else:
            sorted = True
    return count

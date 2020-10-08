import math


def resilient(n):
    count = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            count += 1
    return count


def compute(num, ratio):
    min_d = 10**9 + 1
    for n in range(2, num):
        resilient_fraction = resilient(n)
        r = resilient_fraction / (n-1)
        if r < ratio:
            min_d = min(min_d, n)

    return min_d


print(compute(94744, (15499/94744)))
        

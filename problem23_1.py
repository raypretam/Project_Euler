from math import sqrt
import time

start = time.time()

def divisors(n):
    sum = 1
    t = sqrt(n)
    # only proper divisors; start from 2.
    for i in range(2, int(t)+1):
        if n % i == 0:
            sum += i + n / i
    # don't count the square root twice!
    if t == int(t):
        sum -= t
    return sum

limit = 28123
non_ab_sum = 0
ab = set()
for i in range(12,limit):
    if divisors(i) > i:
        ab.add(i)
    if not any((i-a in ab) for a in ab):
        non_ab_sum += i
print(non_ab_sum)
print(time.time() - start)


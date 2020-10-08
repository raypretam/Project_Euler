from itertools import permutations
import time


def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


start = time.time()

p1 = list(permutations('987654321'))
p2 = list(permutations('87654321'))
p3 = list(permutations('7654321'))
p4 = list(permutations('654321'))
p5 = list(permutations('54321'))
p6 = list(permutations('4321'))
p7 = list(permutations('321'))

out = p1 + p2 + p3 + p4 + p5 + p6 + p7

filtered = [int("".join(x)) for x in out]
prime = [x for x in filtered if is_prime(x)]

print(max(prime))
print("It took {}s".format(time.time() - start))

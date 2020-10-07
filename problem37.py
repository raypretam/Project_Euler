"""
The number 3797 has an interesting property. Being prime itself, it is possible 
to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable 
from left to right and right to left.
"""
import time


# Sieve of Eratosthenes
def sieve(n):
    multiples = set()
    prime = []
    for i in range(2, n+1):
        if i not in multiples:  # O(1) time lookup as it is a set
            prime.append(i)
            multiples.update(set(range(i*i, n+1, i)))  # putting all the multiples of a number into the set
    return prime


def truncatable_prime(n):
    primelist = [str(x) for x in sieve(n)[::-1]]
    primeset = set(primelist)
    truncatable_left = set()
    truncatable_right = set()

    for n in primelist:
        # n = 'abc'; [n[i:] for i in range(len(n))] -> ['abc', 'bc', 'c']
        alltruncs_left = set(n[i:] for i in range(len(n)))
        # Checks if the subset like above is in the above primeset
        if alltruncs_left.issubset(primeset):  
            truncatable_left.add(int(n))  # if the subset exists then put n in the set

        # n = 'abc'; [n[i:] for i in range(len(n))] -> ['abc', 'ab', 'a']
        alltruncs_right = set(n[:i+1] for i in range(len(n)))
        if alltruncs_right.issubset(primeset):
            truncatable_right.add(int(n))  # similarly as above

    # we have find the intersection of both the sets to find primes which are 
    # both left and right truncatable.
    # As the question suggests that 2,3,5,7 are not prime .
    return (truncatable_left.intersection(truncatable_right)).difference((2, 3, 5, 7))


start = time.time()
# printing the sum of the set we found
print(sum(truncatable_prime(10**6)))  # I assumed the upper bound to be 1 million. No reason I could come up with
print("It took {}s".format(time.time() - start))

"""
It was proposed by Christian Goldbach that every odd composite number can be 
written as the sum of a prime and twice a square.
It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as 
 the sum of a prime and twice a square?
"""
import time


# finding all the prime numbers
def sieve(n):
    primes = []
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            multiples.update(set(range(i*i, n+1, i)))
    return primes


# checking for if the diff is 2*some square number
def is_twice_square(n):
    sqr_test = (n//2)**0.5
    return sqr_test == int(sqr_test)


def conjecture():
    primes = sieve(10**5)
    ans = 1
    notFound = True

    while notFound:
        ans += 2  # increasing the number by 2
        j = 0
        notFound = False  # notFound is first set to false so that we can break out of the loop
        while (ans >= primes[j]):
            # if square number is found notFound is set to true the loop runs again
            if is_twice_square(ans - primes[j]):
                notFound = True  # set it to true for the next iteration
                break  # break the loop for the next step
            # checking if the next prime number satisfies the conjecture
            j += 1  # checking all the primes until we reach that number

    return ans


start = time.time()
print(conjecture())
print("It took {}s".format(time.time() - start))
    



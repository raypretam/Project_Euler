"""
If we take a number nn, we can bound it's number of digits d to : 10^(d−1)≤n<10^d
Let's say we form a d digit long number of all 9 as the maximum, the sum of it's factorial digits would be 9!d

From the above eqn d is d>=7
"""

from math import factorial
import time


start = time.time()

# factorials of numbers from 0-9
f = [factorial(0),
     factorial(1),
     factorial(2),
     factorial(3),
     factorial(4),
     factorial(5),
     factorial(6),
     factorial(7),
     factorial(8),
     factorial(9)]


# sum of factorial of the digits
def factorial_digits(n):
    s = 0
    while n:
        s += f[n % 10]
        n //= 10
    return s


solution = 0
for i in range(10, 2540160):
    if factorial_digits(i) == i:
        solution += i

# printing the solution
print(solution)
end = time.time()
print("It took {}s".format(end - start))

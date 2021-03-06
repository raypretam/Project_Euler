"""
    an = (9,25,49,81,121,...) = 4*n**2 + 4*n + 1
    bn = (5,17,37,65,101,...) = 4*n*2 + 1
    cn = (3,13,31,57,91,...) = 4*n**2 - 2*n +1
    dn = (7,21,43,73,111,...) = 4*n**2 + 2*n + 1
    for all values of n[1,...]

    sn = 1 + an + bn + cn + dn
"""


def solution(n):
    n = (n - 1) / 2
    return 2 * n * (8 * n * n + 15 * n + 13) // 3 + 1


print(solution(1001))

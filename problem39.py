from collections import defaultdict
import time


def check_sides(a, b, c):
    return a + b > c and b + c > a and a + c > b


def check_right_triangle(a, b, c):
    return a**2 + b**2 == c**2


def run(p):
    perimeter = defaultdict(list)
    for a in range(3, p+1):
        for b in range(4, p+1):
            c = int((a**2 + b**2)**0.5)
            if check_right_triangle(a, b, c) and check_sides(a, b, c):
                perimeter[a+b+c].append([a, b, c])
    
    max_count = 0
    ans = 0
    for k in perimeter.keys():
        if max_count < len(perimeter[k]) and k <= 1000:
            max_count = len(perimeter[k])
            ans = k

    return ans


start = time.time()
print(run(1000))
print(time.time() - start)



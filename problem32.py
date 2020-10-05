import time
pandigital = set()


def is_pandigital(a, b):
    if len(str(a) + str(b) + str(a*b)) == 9 and set(str(a) + str(b) + str(a*b)) == set('123456789'):
        pandigital.add(a*b)
    else:
        return


for i in range(1, 10):
    for j in range(1000, 10000):
        is_pandigital(i, j)

for i in range(10, 100):
    for j in range(100, 1000):
        is_pandigital(i, j)


start = time.time()
print(sum(pandigital))
print("It took {}s".format(time.time() - start))

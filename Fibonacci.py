# simple:
def get_sequence(n):
    a = 0
    b = 1
    sequence = []
    for i in range(n):
        if i > 1:
            a, b = b, (a + b)
            sequence.append(b)
        else:
            sequence.append(i)
    return sequence

results = get_sequence(100)
print(results)

############################################################
# recursive:
############################################################


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

for i in range(1,20):
    print(fib(i))

############################################################
# loop
############################################################

def fib2(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a + b
    return(a)

for i in range(1,20):
    print(fib2(i))

############################################################
# generator
############################################################

def fib3():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

n = 0
for i in fib3():
    if n > 20:
        break
    print(i)
    n += 1


############################################################
# cached
############################################################
fib_cache = {}
def fib4(n):
    if n in fib_cache:
        return fib_cache[n]

    if n == 1 or n == 2:
        return 1
    value = fib4(n-1) + fib4(n-2)

    fib_cache[n] = value
    return value

for i in range(1, 2000):
    print(fib4(i))

############################################################
# memoize
############################################################
from functools import lru_cache

@lru_cache(maxsize=None)
def fib5(n):
    return n if n < 2 else fib5(n-2) + fib5(n-1)

for i in range(1, 200):
    print(fib5(i))
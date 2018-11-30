# BASICALLY IGNORE THIS FILE. IT'S ALL JUST IDEAS MORE THAN ANYTHING.


# Number 1
def isprime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def primesum(n):
    total = 0
    for i in range(n):
        prime = isprime(n)
        if prime is True:
            total = total + n
        return total

print(primesum(3))


# Number 2 - Actually correct
def sumsquares(n):
    i = 1
    l = []
    while (i * i < n):
        l += [i * i]
        i += 1
    return l


print(sumsquares(5))


# Number 3
def primefactors(n):
    l = []
    for i in range (2, n + 1):
        num = isprime(n)
        if num <= n:
            l = l + num
        return l

# Number 4
# Number 5
# Number 6
# Number 7

def PascalsPrettyLittleTriangle(n):
    n1 = [n]
    n2 = [n, n]
    n3 = [n+n, n+n, n+n]

# Number 8
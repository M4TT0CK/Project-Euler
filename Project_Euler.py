import math

def sieveOfEratosthenes(n):
    list = [True] * (n + 1)
    list[0] = False
    list[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if list[i] == True:
            c = 0
            j = i ** 2
            while j <= n:
                list[j] = False
                j = (i ** 2) + (c * i)
                c += 1
    primes = []
    h = 0
    for x in list:
        if x == True:
            primes.append(h)
        h += 1
    
    return primes
import math
import Project_Euler
# Problem 7: What is the 10001st prime number?

# Iterates through each integer 2...n until the correct prime is found.
# Runtime is very long using standard sieve; needs revision
def nthPrime(n):
    p = []
    index = 2

    while len(p) < n:
        p = []
        for x in Project_Euler.sieveOfEratosthenes(index):
            p.append(x)
        print(len(p))
        index += 1
    
    return p[n - 1]

print(nthPrime(10001)) # Solution: 104743
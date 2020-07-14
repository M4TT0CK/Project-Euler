import math
import Project_Euler
# Problem 7: What is the 10001st prime number?

# Uses a simple primality function and iterates up to the desired index.
# Least expensive solution so far.
def nthPrime(n):
    p = [2]
    index = 3
    length = 0

    while length != n:
        length = len(p)
        if Project_Euler.isPrime(index):
            p.append(index)
        index += 2
    
    return p[n - 1]

print(nthPrime(10001)) # Solution: 104743
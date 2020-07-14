import math
import Project_Euler
# Problem 7: What is the 10001st prime number?

# Enlarges the number to run through the sieve by a scale factor of 50 with each
# iteration. Once the length of the array returned outstrips tne index needed,
# the array index is called, thus providing the solution.
def nthPrime(n):
    p = []
    index = 1
    length = 0
    last = 0

    while length != n:
        length = len(p)
        if length < n:
            last = index
            index = index * 50
            p = Project_Euler.sieveOfEratosthenes(index)
        if length > n:
            return p[n - 1]
        print(length)
    
    return p[n - 1]

print(nthPrime(10001)) # Solution: 104743
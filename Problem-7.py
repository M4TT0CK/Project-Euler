import math
import Project_Euler
# Problem 7: What is the 10001st prime number?

# Uses a sort of binary search approach to locate a prime by index.
# It doubles in size with every iteration such that the current index < n.
# If index > n, spltis the difference of iteration and subtracts to back track.
# Takes considerably less time to find the answer this way than through a
# strictly iterative approach.
def nthPrime(n):
    p = []
    index = 1
    length = 0
    last = 0

    while length != n:
        length = len(p)
        if length < n:
            last = index
            index = index * 2
            p = Project_Euler.sieveOfEratosthenes(index)
        if length > n:
            index = index - int((index - last) / 2)
            p = Project_Euler.sieveOfEratosthenes(index)
        print(len(p))
    
    return p[n - 1]

print(nthPrime(10001)) # Solution: 104743
import math
# Problem 3: What is the largest prime factor of the number 600851475143 ?

def largestPrimeFactor(n):
    largestPrime = 0
    
    # Since our n is odd, we start at 3 and iterate by 2 each time up to
    # square root of n, which the largest prime factor must be smaller than
    for i in range(3, int(math.sqrt(n)) + 2, 2):
        # If n % i == 0, then i is a prime factor and is thus our new largest prime factor
        while n % i == 0:
            largestPrime = i
            n = n / i # Removes all occurrences of i from n
    
    return largestPrime
    
print(largestPrimeFactor(600851475143)) # Answer: 6857
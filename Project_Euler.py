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

# Source: https://www.w3schools.com/python/python_for_loops.asp
def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
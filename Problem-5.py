import math
# Problem 5: What is the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20?

# Finds prime factors for a given n
def primeFactors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(int(i))
            n = n / i

    if n > 2:
        factors.append(int(n))
    
    return factors

factorsList = []
degreesList = []
product = 1

# Populates list of prime factors for 2...20 (1 is a freebie)
for i in range(2, 21):
    factorsList.append(primeFactors(i))
    degreesList.append(0)

# Determines the highest degree for each number 2...20 and logs it
for i in range(2, 21):
    for j in factorsList:
        if j.count(i) > degreesList[i - 2]:
            degreesList[i - 2] = j.count(i)

# Keeps a rolling product of each number 2...20 raised to their highest degree
for i in range(2, 21):
    product = product * (i ** degreesList[i - 2])

print(product) # Solution: 232792560
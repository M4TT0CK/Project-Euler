# Problem 1: Find the sum of all the multiples of 3 or 5 below 1000

sum = 0 # Rolling sum

# Iterates x...999; if x is divisible by 3 or 5, x is added to rolling sum
for x in range(1000):
    if (x % 3 == 0) or (x % 5 == 0):
        sum += x

print(sum) # Answer: 233168
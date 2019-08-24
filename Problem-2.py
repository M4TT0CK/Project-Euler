# Problem 2: By considering the terms in the Fibonacci sequence whose 
# values do not exceed four million, find the sum of the even-valued terms

sum = 0 # Rolling sum
phi = (1 + (5**.5)) / 2
psi = (1 - (5**.5)) / 2
fib = 0 # Placeholder variable for the given Fibonacci number
x = 0 # Rolling x value

while fib <= 4000000:
    # Calculuates Fibonacci number for a given x using Binet's formula
    fib = int((phi**x - psi**x) / (5**.5))
    if (fib % 2) == 0: # Checks for evenness
        sum += fib # Adds to rolling sum
    x += 1 # Iterates x

print(sum)
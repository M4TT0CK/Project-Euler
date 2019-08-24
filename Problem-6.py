# Summation formula raised to the second degree
def squareOfSum(n):
    return int((n * (n + 1)) / 2) ** 2
# Summation of squares formula
def sumOfSqures(n):
    return int((n * (n + 1) * (2 *n + 1)) /6)

print(squareOfSum(100) - sumOfSqures(100)) # Solution: 25164150
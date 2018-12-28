sum = 0
phi = (1 + (5**.5)) / 2
psi = (1 - (5**.5)) / 2
fib = 0
x = 0

while fib <= 4000000:
    fib = int((phi**x - psi**x) / (5**.5))
    if (fib % 2) == 0:
        sum += fib
    x += 1

print(sum)
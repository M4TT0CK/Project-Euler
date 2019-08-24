# Problem 4: Find the largest palindrome made from the product of two 3-digit numbers

def palindromeCheck(n):
    digits = [int(x) for x in str(n)] # Decompose digits into a list

    for i in range(0, int(len(digits) / 2), 1):
        # If at any point palindrome pattern is broken, return false
        if digits[i] != digits[len(digits) - i - 1]:
            return False

    return True

largest = 0

for i in range(999, 100, -1):
    j = i
    # Sub-index j sets to current i, because multiplication is commutative
    while j >= 100:
        product = i * j
        # Checks if product is palindrome AND bigger than current largest held value
        # This could probably be more efficient with better python knowledge
        if palindromeCheck(product) == True and product > largest:
            largest = product
            # Breaks out of while loop if a palindrome is found due to diminishing returns
            break
        j -= 1

print(largest) # Solution: 906609
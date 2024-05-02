"""
find the sum of all the primes below 2 million
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

n = 2000000
total = 0
for i in range(n):
    if is_prime(i):
        total += i
print(total)
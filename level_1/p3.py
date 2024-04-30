"""
largest prime factor of the number 600851475143
"""

import math
import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

max_factor = 1
n = 600851475143
for i in range(int(math.sqrt(n)) // 2, 1, -1):
    if n % i == 0 and is_prime(i):
        max_factor = i
        break

print(max_factor)

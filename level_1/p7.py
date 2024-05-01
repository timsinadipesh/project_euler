"""
find the 10001st prime number
"""

import sys
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

num = 1
num_prime = 0
while True:
    if is_prime(num):
        num_prime += 1
        if num_prime == 10001:
            print(num)
            sys.exit()
    num += 1
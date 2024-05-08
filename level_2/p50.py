# find the prime below one-million which is the 
# sum of the most consecutive primes

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = 1000000
primes = [k for k in range(2, n) if is_prime(k)]
max_length = 0
max_sum = 0

for i in range(len(primes)):
    for j in range(i + max_length, len(primes)):
        current_sum = sum(primes[i:j])
        if current_sum >= n:
            break
        if is_prime(current_sum) and (j - i) > max_length:
            max_length = j - i
            max_sum = current_sum

print(max_length, max_sum)
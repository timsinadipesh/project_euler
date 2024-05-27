# find the largest n-digit pandigital prime

from helpers import is_prime

def is_pandigital(n):
    nst = str(n)
    l = len(nst)
    return ''.join(sorted(nst)) == '123456789'[:l]

# test: is_pandigital(n)
# print(1, is_pandigital(1))
# print(2143, is_pandigital(2143))
# print(87654321, is_pandigital(87654321))
# print(237480, is_pandigital(237480))

# since the sum of any n-digit pandigital number 
# other than n=4,7 and n>2 is divisible by 3, 
# we start with max 7-digit pandigital number
for i in range(7652413, 1, -2): 
    if is_pandigital(i) and is_prime(i):
        print(i)
        break
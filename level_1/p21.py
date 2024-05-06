# find the sum of all the amicable numbers under n

def sum_divisors(n):
    tot = 1
    sqrt_n = int(n ** 0.5)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            tot += i + n // i
    if sqrt_n * sqrt_n == n:
        tot -= sqrt_n  
    return tot

n = 10000
tot = 0
for i in range(1, n):
    d_a = sum_divisors(i)
    d_i = sum_divisors(d_a)
    if i != d_a and i == d_i:
        tot += d_a
print(tot)
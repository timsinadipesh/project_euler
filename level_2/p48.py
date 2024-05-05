# prints the last 10 digits of a series
# 1**1 + 2**2 + ... + n**n

def sum_series(n):
    tot = 0
    for i in range(1, n+1):
        tot += i**i
    return tot

for n in [10, 1000]:
    digits = sum_series(n)
    print(str(digits)[-10:])
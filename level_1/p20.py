# find the sum of the digits in the number n!

def fac(n):
    tot = 1
    for i in range(n, 1, -1):
        tot *= i
    return tot

n = 100
st = str(fac(n))
tot = 0
for c in st:
    tot += int(c)
print(tot)
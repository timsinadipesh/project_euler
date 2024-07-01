"""
sum of all the multiples of 3 or 5 upto 1000
"""

def sum_divisibles_upto(target, divisor):
    upperlimit = target // divisor
    tot = 0
    for i in range(upperlimit+1):
        tot += i
    return tot * divisor

n = 999
total =  sum_divisibles_upto(n, 3) + sum_divisibles_upto(n, 5) - sum_divisibles_upto(n, 15)
print(total)
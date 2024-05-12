# find the sum of all numbers which are equal to
# the sum of the factorial of their digits

from math import factorial

tot = 0
for i in range(3, 100000):
    st = str(i)
    num_sum = 0
    for c in st:
        num_sum += factorial(int(c))
    if num_sum == i:
        print(i)
        tot += num_sum
print(tot)
"""
find the difference between the sum of the squares of 
the first one hundred natural numbers and the square of the sum
"""

sq_sum = 0
total = 0
for i in range(1, 101):
    total += i
    sq_sum += i**2

total_sq = total**2

print(total_sq - sq_sum)
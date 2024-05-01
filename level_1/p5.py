"""
find the smallest positive number that is 
evenly divisible by all of the numbers from 1 to 20
"""

import sys

num = 2500 # starting num, which is evenly divisible by all from 1 to 10
lst = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11] 
while True:
    found = True
    for i in lst:
        if num % i != 0:
            found = False
            break
    if found:
        print(num)
        sys.exit(0)
    num += 20
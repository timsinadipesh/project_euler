# a grid of certain length is given
# starting on the top left corner
# how many ways are there to reach the bottom right cornor
# when only allowed to move to the right and down

from math import comb

def num_ways(n: int) -> int:
    return comb(2*n, n) # binomial coefficient 

for i in range(0, 24, 5):
    print("n =", i, ":", num_ways(i))
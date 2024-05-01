"""
find the largest palindrome made from 
the product of two 3-digit numbers
"""

largest_pali = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        prod = i * j
        st = str(prod)
        if st == st[::-1] and prod > largest_pali:
            largest_pali = prod
            print(i, j, prod)

print(largest_pali)
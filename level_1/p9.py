"""
find the product of the only one pythagorean triplet 
for which a + b + c = 1000
"""

tar = 1000
for i in range(1, tar):
    for j in range(i+1, tar):
        for k in range(j+1, tar):
            if i + j + k == tar and i**2 + j**2 == k**2:
                print(i * j * k)
            
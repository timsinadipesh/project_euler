# find the millionth lexicographic permutation 
# of the digits from 0 to 9

from math import factorial as fac

def get_nth_permutation(digits, perm_num):
    perm = ""
    n = len(digits)
    perm_num -= 1

    for i in range(1, n):
        j = perm_num // fac(n - i)
        perm_num = perm_num % fac(n - i)
        perm += str(digits[j])
        digits.pop(j)
        if perm_num == 0:
            break
    
    for dig in digits:
        perm += str(dig)
    
    return perm

digits = list(range(10))
perm_num = 1000000
print(get_nth_permutation(digits, perm_num))
# find the sum of the only eleven primes that are
# both truncatable from left to right and right to left

import helpers

def remove_from_left(num):
    n = str(num)
    lst = [num]
    for i in range(1, len(n)):
        lst.append(n[i:])
    return list(map(int, lst))

# test: remove_from_left(num)
# print(remove_from_left(1324))

def remove_from_right(num):
    n = str(num)
    lst = [num]
    for i in range(1, len(n)):
        lst.append(n[:-i])
    return list(map(int, lst))

# test: remove_from_right(num)
# print(remove_from_right(1325))

tar_prime = 0
primes_lst = []
tot = 0
mv_num = 11
while tar_prime < 11:
    if helpers.is_prime(mv_num):
        nums = remove_from_left(mv_num) + remove_from_right(mv_num)
        if all(helpers.is_prime(num) for num in nums):
            tot += mv_num
            tar_prime += 1
            primes_lst.append(mv_num)
    mv_num += 2
print(tot)
print(primes_lst)
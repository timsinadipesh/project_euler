# find the number of circular primes below one million

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# test: is_prime(n)
# print(is_prime(1))
# print(is_prime(2))
# print(is_prime(3))
# print(is_prime(23))

def get_rotations(num):
    digits = list(str(num))
    nums = []
    for i in range(len(digits)):
        curr_dig = digits.pop(0)
        tmp_num = ''.join(digits)
        nums.append(curr_dig + tmp_num)
        digits.append(curr_dig)
    return nums

# test: get_rotations(num)
# print(get_rotations('12'))
# print(get_rotations('123'))
# print(get_rotations('1234'))

# process
def get_num_circular_primes(n):
    circular_primes = set()
    for i in range(n):
        if is_prime(i) and i not in circular_primes:
            nums = list(map(int, get_rotations(i)))

            all_primes = True
            for num in nums:
                if not is_prime(num):
                    all_primes = False
                    break
            if all_primes:
                circular_primes.update(nums)
    return len(circular_primes)

# test: get_num_circular_primes(n)
print(get_num_circular_primes(100))
print(get_num_circular_primes(1000000))
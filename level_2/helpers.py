def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# test: is_prime(n)
print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(23))
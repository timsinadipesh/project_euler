# find the sum of all the numbers, less than one million,
# which are palindromic in base 10 and base 2

def to_binary(n):
    binary = ""
    while n > 0:
        rem = n % 2
        binary = str(rem) + binary
        n //= 2
    return binary


def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]


print("binary test")
print(0, "->", to_binary(0))
print(1, "->", to_binary(1))
print(2, "->", to_binary(2))
print(10, "->", to_binary(10))
print("-"*40)
print("palindrome test")
print(2034, "->", is_palindrome(2034))
print(101, "->", is_palindrome(101))
print("-"*40)

# process
tot = 0
for base10 in range(1, 1000000):
    base2 = int(to_binary(base10))
    if is_palindrome(base10) and is_palindrome(base2):
        tot += base10
print("Total:", tot)
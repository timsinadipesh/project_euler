# find the index of the first term in the fibonacci seq
# to contain n digits

def fib_with_digits(n):
    a, b = 1, 1
    count = 2
    while True:
        a, b = b, a + b
        count += 1
        if len(str(b)) == n:
            return count

print(fib_with_digits(3))
print(fib_with_digits(1000))
"""
find the sum of the even-valued terms
in the fibonacci sequence up to 4 million
"""

def fibonacci():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()

total = 0
num = next(fib)
while num < 4000000:
    if num % 2 == 0:
        total += num
    num = next(fib)

print(total)
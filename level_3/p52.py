# find the smallest positive integer, x, such that
# 2x, 3x, 4x, 5x, 6x, contain the same digits

def same_digits(a, b):
    return sorted(str(a)) == sorted(str(b))

x = 1
while True:
    if same_digits(x, 2 * x) and \
    same_digits(x, 3 * x) and \
    same_digits(x, 4 * x) and \
    same_digits(x, 5 * x) and \
    same_digits(x, 6 * x):
        break
    x += 1

print(x)
for i in range(2, 7):
    print(i * x)

# find the largest 1 to 9 pandigital 9-digit number
# that can be formed as the concatenated product of
# an integer with (1,2,...,n) where n > 1

pandigitals = []
for i in range(1, 10000):
    n = 1
    s = ''
    while len(s) < 9:
        s += str(i * n)
        n += 1
    if len(s) == 9 and ''.join(sorted(s)) == '123456789':
        pandigitals.append((int(s), i, n - 1))
print(max(pandigitals))
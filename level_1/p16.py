# sum of the digits of a number(a) raised to a certain power(n)

def sum_digits(a, n):
    num = a**n
    st = str(num)
    tot = 0
    for c in st:
        tot += int(c)
    return tot

print(sum_digits(2, 1000))
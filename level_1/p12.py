# find the value of the first triangle number
# to have over five hundred divisors

def get_tri_num(n):
    return n * (n + 1) // 2

def get_div_count(n):
    count = 0
    for i in range(1, int(n**(1/2))):
        if n % i == 0:
            count += 2
    return count

tri_num = 1
div_count = 0
tri_num_idx = 1

while div_count < 500:
    tri_num = get_tri_num(tri_num_idx)
    tri_num_idx += 1

    div_count = get_div_count(tri_num)

print(tri_num)